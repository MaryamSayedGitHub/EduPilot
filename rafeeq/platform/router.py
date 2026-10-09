from fastapi import APIRouter, File, Form, UploadFile
from rafeeq.samples import load_sample
from rafeeq.snap.reader import read_snap
router = APIRouter(tags=["M1 platform"])

# Temporary: one demo account. Replaced with a real database check later.
DEMO_USER = {"token": "demo-token-sara-123", "user_id": "u_sara", "name": "سارة أحمد", "role": "student"}


@router.post("/auth/login")
def login(body: dict):
    return DEMO_USER

@router.get("/rooms")
def list_my_rooms():
    return load_sample("my_rooms")

@router.post("/rooms/{room_id}/files", status_code=202)
def upload_file(room_id: str, file: UploadFile = File(...)):
    return load_sample("upload_file")

@router.post("/snap")
async def snap_and_ask(
    photo: UploadFile = File(...),
    room_id: str | None = Form(None),
):
    photo_bytes = await photo.read()
    return read_snap(photo_bytes)
