Chat API with FastAPI and OpenAI
This project is a FastAPI-based web application that integrates with OpenAI's API to provide a chat interface and stores conversation history in a SQLite database.
Features

RESTful API for chat interactions using FastAPI
Integration with OpenAI's GPT-3.5-turbo model
SQLite database for storing chat history
CORS support for cross-origin requests
Static file serving for front-end assets
Environment variable management with python-dotenv

Prerequisites

Python 3.8+
SQLite
OpenAI API key

Installation

Clone the repository:

git clone <repository-url>
cd <repository-directory>


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Set up the environment variable:


Create a .env file in the root directory
Add your OpenAI API key:

OPENAI_API_KEY=your-api-key-here

Usage

Start the FastAPI server:

uvicorn main:app --reload


Access the API:


The API will be available at http://localhost:8000
Use the /chat endpoint to send POST requests with JSON payload:

{
    "user_input": "Your message here"
}


Access static files:


Static files are served from the /static directory at http://localhost:8000/static


View API documentation:


Interactive API docs are available at http://localhost:8000/docs

Database

The application uses SQLite to store chat history
The database file database.db is created automatically in the project root
Chat history is stored in the chats table with columns: id, user_input, and response

Project Structure
project/
│
├── main.py           # FastAPI application
├── database.db       # SQLite database file
├── .env             # Environment variables
├── requirements.txt  # Python dependencies
├── static/          # Static files directory

Endpoints

POST /chat: Send a user message to get a response from OpenAI's GPT-3.5-turbo
Request body: { "user_input": "string" }
Response: { "response": "string" } or { "error": "string" }



Notes

Ensure your OpenAI API key is valid and has sufficient credits
The .env file should not be committed to version control
The application runs in debug mode with --reload for development

License
This project is licensed under the MIT License.
