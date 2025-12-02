"""Convenience script to start the FastAPI inference service."""
from uvicorn import run


if __name__ == "__main__":
    run("api_service:app", host="0.0.0.0", port=8000, reload=False)
