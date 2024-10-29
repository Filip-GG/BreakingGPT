from  fastapi import FastAPI, Request
from pydantic import BaseModel
from model import query

app = FastAPI()
config = 'config.json'

class Query(BaseModel):
    query : str

@app.post('/')
async def read_root(data: Query):
    out = query(data.query, config)
    return out

