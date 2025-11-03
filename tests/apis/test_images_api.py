from unittest.mock import AsyncMock, patch

import pytest

from app.apis.images_api import get_image


class DummyResponse:
    def __init__(self, status_code=200, json_data=None, text=""):
        self.status_code = status_code
        self._json = json_data
        self.text = text

    def json(self):
        return self._json


@pytest.mark.asyncio
async def test_get_image_single(monkeypatch):
    data = {
        "user": {"name": "Alice"},
        "urls": {"regular": "https://example.com/a.jpg"},
    }

    async def mock_get(url, params=None):
        return DummyResponse(status_code=200, json_data=data)

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(side_effect=mock_get)

    # Patch httpx.AsyncClient to return our mock client as a context manager
    class MockAsyncClient:
        def __init__(self, *args, **kwargs):
            pass

        async def __aenter__(self):
            return mock_client

        async def __aexit__(self, exc_type, exc, tb):
            return False

    with patch("app.apis.images_api.httpx.AsyncClient", MockAsyncClient):
        res = await get_image(1, query="test")
        assert res == {"author": "Alice", "image_url": "https://example.com/a.jpg"}


@pytest.mark.asyncio
async def test_get_image_multiple(monkeypatch):
    data = [
        {"user": {"name": "A"}, "urls": {"regular": "https://example.com/a.jpg"}},
        {"user": {"name": "B"}, "urls": {"regular": "https://example.com/b.jpg"}},
    ]

    async def mock_get(url, params=None):
        return DummyResponse(status_code=200, json_data=data)

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(side_effect=mock_get)

    class MockAsyncClient:
        async def __aenter__(self):
            return mock_client

        async def __aexit__(self, exc_type, exc, tb):
            return False

    with patch("app.apis.images_api.httpx.AsyncClient", MockAsyncClient):
        res = await get_image(2, query="test")
        assert isinstance(res, list)
        assert res[0]["author"] == "A"
        assert res[1]["image_url"] == "https://example.com/b.jpg"


@pytest.mark.asyncio
async def test_get_image_unsplash_error(monkeypatch):
    async def mock_get(url, params=None):
        return DummyResponse(status_code=500, json_data={"error": "boom"}, text="boom")

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(side_effect=mock_get)

    class MockAsyncClient:
        async def __aenter__(self):
            return mock_client

        async def __aexit__(self, exc_type, exc, tb):
            return False

    from fastapi import HTTPException

    with patch("app.apis.images_api.httpx.AsyncClient", MockAsyncClient):
        with pytest.raises(HTTPException):
            await get_image(1, query="test")
