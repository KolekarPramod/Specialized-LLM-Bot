import os
import tempfile
import pandas as pd
from typing import List, Dict, Tuple
import gradio as gr
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class PDFProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", ".", " ", ""]
        )
    
    def extract_text(self, pdf_file) -> str:
        """Extract text from a PDF file."""
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            # Handle both file-like objects and file paths
            if hasattr(pdf_file, 'name'):
                # It's a file object from Gradio
                temp_file_path = pdf_file.name
                text = self._extract_from_path(temp_file_path)
            else:
                # It's raw bytes or needs to be saved first
                temp_file.write(pdf_file)
                temp_file_path = temp_file.name
                text = self._extract_from_path(temp_file_path)
                # Clean up the temporary file
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)
            
            return text
    
    def _extract_from_path(self, file_path: str) -> str:
        """Extract text from a PDF at the given file path."""
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    
    def split_text(self, text: str) -> List[str]:
        """Split the text into manageable chunks."""
        return self.text_splitter.split_text(text)

class QAGenerator:
    def __init__(self, model_name="llama2"):
        self.llm = Ollama(model=model_name)
        
        self.simple_qa_prompt = PromptTemplate(
            input_variables=["context"],
            template="""
            Based on the following text, generate 2 factual question-answer pairs that have SHORT, direct answers.
            
            Text: {context}
            
            Format each pair as "Q: [question]" on one line and "A: [answer]" on the next line, with an empty line between pairs.
            """
        )
        
        self.complex_qa_prompt = PromptTemplate(
            input_variables=["context"],
            template="""
            Based on the following text, generate 2 complex question-answer pairs. These should require deeper analysis or broader understanding of the content.
            
            Text: {context}
            
            Format each pair as "Q: [question]" on one line and "A: [answer]" on the next line, with an empty line between pairs.
            Make sure the answers are comprehensive and at least 2-3 sentences long.
            """
        )
        
        self.simple_chain = LLMChain(llm=self.llm, prompt=self.simple_qa_prompt)
        self.complex_chain = LLMChain(llm=self.llm, prompt=self.complex_qa_prompt)
    
    def generate_qa_pairs(self, chunks: List[str], progress=None) -> List[Dict[str, str]]:
        """Generate Q&A pairs from text chunks."""
        qa_pairs = []
        
        total_chunks = len(chunks)
        for i, chunk in enumerate(chunks):
            if progress is not None:
                progress(i/total_chunks, f"Processing chunk {i+1}/{total_chunks}")
            
            # Generate simple QA pairs
            simple_result = self.simple_chain.run(context=chunk)
            qa_pairs.extend(self._parse_qa_output(simple_result))
            
            # Generate complex QA pairs
            complex_result = self.complex_chain.run(context=chunk)
            qa_pairs.extend(self._parse_qa_output(complex_result))
        
        return qa_pairs
    
    def _parse_qa_output(self, output: str) -> List[Dict[str, str]]:
        """Parse the LLM output into structured Q&A pairs."""
        pairs = []
        lines = output.strip().split("\n")
        
        i = 0
        while i < len(lines):
            if lines[i].startswith("Q:"):
                question = lines[i][2:].strip()
                if i + 1 < len(lines) and lines[i + 1].startswith("A:"):
                    answer = lines[i + 1][2:].strip()
                    pairs.append({"question": question, "answer": answer})
                i += 2
            else:
                i += 1
        
        return pairs

def process_pdf(pdf_file, model_name, progress=gr.Progress()):
    """Process a PDF file and generate Q&A pairs."""
    try:
        progress(0, "Initializing...")
        processor = PDFProcessor()
        
        progress(0.1, "Extracting text from PDF...")
        text = processor.extract_text(pdf_file)
        
        progress(0.3, "Splitting text into chunks...")
        chunks = processor.split_text(text)
        
        progress(0.4, "Initializing QA Generator...")
        generator = QAGenerator(model_name=model_name)
        
        progress(0.5, "Generating Q&A pairs...")
        qa_pairs = generator.generate_qa_pairs(chunks, 
                                               lambda p, s: progress(0.5 + p * 0.4, s))
        
        # Create pandas DataFrame
        progress(0.9, "Creating dataset...")
        df = pd.DataFrame(qa_pairs)
        
        # Save to CSV
        csv_path = "qa_dataset.csv"
        df.to_csv(csv_path, index=False)
        
        progress(1.0, "Complete!")
        return df, csv_path
    except Exception as e:
        raise gr.Error(f"Error processing PDF: {str(e)}")

# Create Gradio interface
with gr.Blocks(title="PDF Q&A Dataset Generator") as app:
    gr.Markdown("# PDF Q&A Dataset Generator for LLM Fine-tuning")
    gr.Markdown("Upload a PDF and generate question-answer pairs for fine-tuning language models.")
    
    with gr.Row():
        with gr.Column():
            pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
            model_dropdown = gr.Dropdown(
                choices=["llama3.2:3b","llama3.1"], 
                label="Ollama Model", 
                value="llama2"
            )
            generate_btn = gr.Button("Generate Q&A Dataset", variant="primary")
        
        with gr.Column():
            output_csv = gr.File(label="Download Q&A Dataset")
            output_display = gr.DataFrame(label="Generated Q&A Pairs")
    
    generate_btn.click(
        process_pdf,
        inputs=[pdf_input, model_dropdown],
        outputs=[output_display, output_csv]
    )
    
if __name__ == "__main__":
    app.launch()