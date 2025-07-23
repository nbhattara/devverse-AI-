from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI
app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLite DB setup
Base = declarative_base()
engine = create_engine("sqlite:///database.db")
SessionLocal = sessionmaker(bind=engine)

class ChatHistory(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    user_input = Column(Text)
    response = Column(Text)

Base.metadata.create_all(bind=engine)

# Pydantic model
class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.user_input}],
        )
        message = response.choices[0].message["content"].strip()

        # Store in DB
        db = SessionLocal()
        db_chat = ChatHistory(user_input=request.user_input, response=message)
        db.add(db_chat)
        db.commit()
        db.close()

        return {"response": message}
    except Exception as e:
        return {"error": str(e)}
