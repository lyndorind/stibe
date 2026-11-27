from importlib.metadata import version
from fastapi import FastAPI
import uvicorn


__version__ = version("stibe")

app = FastAPI(title="STIBE REST API", version=__version__)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Welcome to STIBE REST API",
        "status": "running"
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/info")
def service_info() -> dict[str, str]:
    return {
        "service": "STIBE REST API",
        "version": app.version
    }


def main() -> None:
    uvicorn.run(app, host="127.0.0.1", port=8000)
