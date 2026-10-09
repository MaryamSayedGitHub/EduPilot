from fastapi import FastAPI
from fastapi.testclient import TestClient

from rafeeq.platform.router import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_snap_returns_result():
    response = client.post(
        "/snap",
        files={"photo": ("page.jpg", b"fake-image", "image/jpeg")},
        data={"room_id": "r_1"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["type"] == "student_work"
    assert body["language"] == "ar"
    assert body["confidence"] == 0.91


def test_snap_needs_a_photo():
    response = client.post("/snap")
    assert response.status_code == 422