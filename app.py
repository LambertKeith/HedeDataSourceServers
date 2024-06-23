from fastapi import FastAPI, HTTPException, Depends, Request, Response
from pydantic import BaseModel
import pytz
from utils.returns_format import ServerState, ServerInfo
from datetime import datetime

server_state = ServerState()
app = FastAPI()

# Define a data model
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


# Define a GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# Define a POST endpoint
@app.post("/data_source/")
def create_item(response: Response, item: Item):
    
    
    return server_state.return_success_info("hello, it's my message")
