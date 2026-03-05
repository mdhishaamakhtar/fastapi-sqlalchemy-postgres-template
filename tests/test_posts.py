import os
from uuid import uuid4
from unittest.mock import patch

from fastapi import status
from fastapi.testclient import TestClient
import pytest

os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")

from database.connection import get_db
from main import app
from schemas.models import DeletePostResponse, Post

client = TestClient(app)

POST_ID = uuid4()
INITIAL_POST_TITLE = "Hello"
INITIAL_POST_DESCRIPTION = "World"
CHANGED_POST_DESCRIPTION = "From the other side"


@pytest.fixture(autouse=True)
def override_db_dependency():
    def fake_get_db():
        yield None

    app.dependency_overrides[get_db] = fake_get_db
    yield
    app.dependency_overrides.clear()


def test_create_post():
    with patch(
        "routes.posts.post_create",
        return_value=Post(
            id=POST_ID, title=INITIAL_POST_TITLE, description=INITIAL_POST_DESCRIPTION
        ),
    ):
        response = client.post(
            "/posts/create",
            json={
                "title": INITIAL_POST_TITLE,
                "description": INITIAL_POST_DESCRIPTION,
            },
        )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["title"] == INITIAL_POST_TITLE
    assert response.json()["description"] == INITIAL_POST_DESCRIPTION


def test_get_all_posts():
    with patch(
        "routes.posts.posts_get_all",
        return_value=[
            Post(
                id=POST_ID,
                title=INITIAL_POST_TITLE,
                description=INITIAL_POST_DESCRIPTION,
            )
        ],
    ):
        response = client.get("/posts/list/all")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


def test_get_one_post():
    with patch(
        "routes.posts.post_get_one",
        return_value=Post(
            id=POST_ID, title=INITIAL_POST_TITLE, description=INITIAL_POST_DESCRIPTION
        ),
    ):
        response = client.get(f"/posts/get/{POST_ID}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == str(POST_ID)
    assert response.json()["title"] == INITIAL_POST_TITLE
    assert response.json()["description"] == INITIAL_POST_DESCRIPTION


def test_patch_post():
    with patch(
        "routes.posts.post_update",
        return_value=Post(
            id=POST_ID, title=INITIAL_POST_TITLE, description=CHANGED_POST_DESCRIPTION
        ),
    ):
        response = client.patch(
            "/posts/update",
            json={
                "id": str(POST_ID),
                "title": INITIAL_POST_TITLE,
                "description": CHANGED_POST_DESCRIPTION,
            },
        )

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == str(POST_ID)
    assert response.json()["title"] == INITIAL_POST_TITLE
    assert response.json()["description"] == CHANGED_POST_DESCRIPTION


def test_delete_post():
    with patch(
        "routes.posts.post_delete",
        return_value=DeletePostResponse(detail="Post Deleted"),
    ):
        response = client.delete(f"/posts/delete/{POST_ID}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["detail"] == "Post Deleted"
