from fastapi import FastAPI

from schemas.schemas import HealthResponse
from routes.posts import router

app = FastAPI()

app.include_router(router=router, prefix="/posts")


@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")
