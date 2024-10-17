from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_ollama import ChatOllama

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize the language model
llm = ChatOllama(
    model="KolekarPramod/hrbot",
    temperature=0,
    # other params...
)

class Message(BaseModel):
    text: str

@app.post("/chat/")
async def chat(message: Message):
    try:
        # Generate a response from the model
        ai_response = llm.invoke(message.text)
        return {"response": ai_response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app with: uvicorn main:app --reload
