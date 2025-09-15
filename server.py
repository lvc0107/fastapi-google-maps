import uvicorn

from app.app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "app.apis.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="trace",
    )
