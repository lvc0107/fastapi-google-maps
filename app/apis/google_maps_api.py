import httpx
from fastapi import APIRouter, Query


router = APIRouter(prefix="/maps", tags=["maps-api"])

UNSPLASH_APP_ID = "823914"
UNSPLASH_ACCESS_KEY = "rfeKBGixCyKXU9mM2ZPoGNYSKUnTLTkFvJqWndz3AuI"
UNSPLASH_SECRET_KEY = "V28mg5c0Y57cK8NC5PYXJOGea2msvSnJgO4mgeHfBDE"




@router.get("/items/{item_id}")
async def get_gmaps_by_id(item_id: int, q: str| None = None):
    return {"item_id": item_id, "q": q}

BASE_URL = "https://api.unsplash.com/photos/random"

@router.get("/image")
async def get_image(query: str = Query("nature")):
    params = {"query": query, "client_id": UNSPLASH_ACCESS_KEY}
    async with httpx.AsyncClient() as client:
        res = await client.get(BASE_URL, params=params)
        data = res.json()
    return {
        "author": data["user"]["name"],
        "image_url": data["urls"]["regular"]
    }