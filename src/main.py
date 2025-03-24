from fastapi import FastAPI
from src.api.v1.routers import router


def create_app() -> FastAPI:

    app = FastAPI()


    app.include_router(router, prefix="/api/v1")
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
