from typing import Union
from fastapi import APIRouter, FastAPI

app = FastAPI()

router = APIRouter(prefix="/hello-world", tags=["hello-world"])


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


