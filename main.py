

from fastapi import FastAPI
import uvicorn
from typing import Union

app = FastAPI()
uvicorn.run(app, host="0.0.0.0")

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

