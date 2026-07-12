from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the FastAPI Web Application
app = FastAPI(title="Text Processing API", description="A simple REST API built with FastAPI")

# 2. Define the Data Model (What kind of data are we expecting from the client?)
class ItemRequest(BaseModel):
    text: str
    uppercase: bool = False

print("\n========================================================")
print(" 🌐 FASTAPI SERVER IS BOOTING UP...")
print("========================================================")

# 3. Create a GET Endpoint (For retrieving data/checking status)
@app.get("/")
def read_root():
    """This is the home page of our API."""
    return {"status": "success", "message": "Welcome to the Text Processing API! The server is live."}

# 4. Create a POST Endpoint (For receiving data, processing it, and sending it back)
@app.post("/process-text/")
def process_text(request: ItemRequest):
    """This endpoint receives a JSON payload, processes the text, and returns the result."""
    original_text = request.text
    
    # Process the text based on the client's request
    if request.uppercase:
        processed_text = original_text.upper()
    else:
        processed_text = original_text.lower()
        
    # Calculate some basic metadata
    character_count = len(original_text)
    word_count = len(original_text.split())
    
    # Return the processed data as a JSON response
    return {
        "original": original_text,
        "processed": processed_text,
        "metadata": {
            "characters": character_count,
            "words": word_count,
            "was_uppercased": request.uppercase
        }
    }

# To run this server, use the command: uvicorn main:app --reload