from fastapi import FastAPI
from fastapi.testclient import TestClient

from rafeeq.platform.router import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_login_returns_the_agreed_fields():
    r = client.post("/auth/login", json={})
    assert r.status_code == 200
    fields = {"token", "user_id", "name", "role"}
    assert set(r.json()) == fields