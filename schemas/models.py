from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    status: str


class Post(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: str

    model_config = ConfigDict(from_attributes=True)


class DeletePostResponse(BaseModel):
    detail: str


class UpdatePost(BaseModel):
    id: UUID
    title: str
    description: str

    model_config = ConfigDict(from_attributes=True)
