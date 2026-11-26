from fastapi import FastAPI
import uvicorn


app = FastAPI(title="STIBE REST API", version="0.1.0")

@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Welcome to STIBE REST API",
        "status": "running"
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


def main() -> None:
    uvicorn.run(app, host="127.0.0.1", port=8000)
