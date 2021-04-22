import pytest
from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

initial_post_title = "Hello"
initial_post_description = "World"
changed_post_description = "From the other side"


@pytest.mark.dependency()
def test_create_post(request):
    response = client.post(
        "/posts/create",
        json={"title": initial_post_title, "description": initial_post_description},
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["title"] == "Hello"
    assert response.json()["description"] == "World"
    request.config.cache.set("post_id", response.json()["id"])


@pytest.mark.dependency(depends=["test_create_post"])
def test_get_all_posts():
    response = client.get("/posts/list/all")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is not None


@pytest.mark.dependency(depends=["test_create_post"])
def test_get_one_post(request):
    post_id = request.config.cache.get("post_id", None)
    response = client.get(f"/posts/get/{post_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == post_id
    assert response.json()["title"] == initial_post_title
    assert (
        response.json()["description"] == initial_post_description
        or changed_post_description
    )


@pytest.mark.dependency(depends=["test_create_post", "test_get_one_post"])
def test_patch_post(request):
    post_id = request.config.cache.get("post_id", None)
    response = client.patch(
        "/posts/update",
        json={
            "id": post_id,
            "title": initial_post_title,
            "description": changed_post_description,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == post_id
    assert response.json()["title"] == initial_post_title
    assert response.json()["description"] == changed_post_description


@pytest.mark.dependency(
    depends=[
        "test_create_post",
        "test_get_one_post",
        "test_patch_post",
        "test_get_all_posts",
    ]
)
def test_delete_post(request):
    post_id = request.config.cache.get("post_id", None)
    response = client.delete(f"/posts/delete/{post_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["detail"] == "Post Deleted"
