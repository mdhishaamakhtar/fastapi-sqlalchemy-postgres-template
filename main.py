from fastapi import FastAPI

from routes.posts import router
from schemas.models import HealthResponse

app = FastAPI()

app.include_router(router=router, prefix="/posts")


@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")
