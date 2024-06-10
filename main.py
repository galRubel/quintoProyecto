

from typing import Union

from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    port =4000
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

