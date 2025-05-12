import gradio as gr
from langchain_ollama import OllamaLLM  # New import

# Use your fine-tuned model
llm = OllamaLLM(model="KolekarPramod/hr_bot_v3")

# Updated chat function for 'messages' type
def chat_fn(message, history):
    try:
        # You can enhance this with memory/context if needed
        response = llm(message)
        return response
    except Exception as e:
        return f"Error: {e}"

# Gradio ChatInterface using new 'messages' format
chat_interface = gr.ChatInterface(
    fn=chat_fn,
    title="Chat with Wrk Talk HR Bot",
    # description="Ask HR-related questions",
    theme="default",
    type="messages"  # ✅ Important fix
)

if __name__ == "__main__":
    chat_interface.launch()
