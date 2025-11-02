import httpx
from fastapi import APIRouter, HTTPException, Path, Query

from app.logging import logger

# from app.services.image_services import ImageService
from app.settings import settings

router = APIRouter(prefix="/maps", tags=["maps-api"])


@router.get("/image/{count}")
async def get_image(
    count: int = Path(..., ge=1, le=10, description="Number of images to fetch (1–10)"),
    query: str = Query("nature", description="Search term for the image"),
):
    """
    Fetch one or more random images from Unsplash by query term.
    """
    logger.info("image_search_start", query=query, count=count)

    params = {"query": query, "count": count, "client_id": settings.unsplash_access_key}

    async with httpx.AsyncClient() as client:
        logger.info(f"URL >>: {settings.unsplash_base_url}")
        res = await client.get(settings.unsplash_base_url, params=params)

    if res.status_code != 200:
        logger.error("unsplash_error", status=res.status_code, body=res.text)
        raise HTTPException(status_code=500, detail="Error from Unsplash API")

    data = res.json()
    logger.info("data_retrieved", data=data)
    # ImageService().save_image_to_db(ImageInfo(**data))

    # If count > 1, Unsplash returns a list; handle both cases
    if isinstance(data, list):
        return [
            {"author": img["user"]["name"], "image_url": img["urls"]["regular"]} for img in data
        ]
    else:
        return {"author": data["user"]["name"], "image_url": data["urls"]["regular"]}
