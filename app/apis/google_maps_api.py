from typing import Union
from fastapi import APIRouter



router = APIRouter(prefix="/gmaps", tags=["google-maps-api"])


@router.get("/")
async def get_gmaps():
    return {"Data": "from Google Maps"}


@router.get("/items/{item_id}")
async def get_gmaps_by_id(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


