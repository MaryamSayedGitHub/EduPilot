from fastapi import APIRouter, File, Form, UploadFile
from pydantic import BaseModel, ConfigDict
from rafeeq.samples import load_sample
from rafeeq.snap.reader import read_snap
from rafeeq.copilot.supervisor import handle_message

router = APIRouter(tags=["M1 platform"])

# Temporary: one demo account. Replaced with a real database check later.
DEMO_USER = {"token": "demo-token-sara-123", "user_id": "u_sara", "name": "سارة أحمد", "role": "student"}

class CopilotRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    room_id: str
    text: str
    file_id: str | None = None

class RegisterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    email: str
    password: str
    role: str
    join_code: str | None = None

class JoinRoomRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    code: str

class CreateRoomRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str

@router.post("/auth/login")
def login(body: dict):
    return DEMO_USER

@router.post("/auth/register")
def register(request: RegisterRequest):
    return load_sample("register")

@router.get("/rooms")
def list_my_rooms():
    return load_sample("my_rooms")

@router.post("/rooms")
def create_room(request: CreateRoomRequest):
    return load_sample("create_room")

@router.post("/rooms/join")
def join_room(request: JoinRoomRequest):
    return load_sample("join_room")

@router.post("/rooms/{room_id}/files", status_code=202)
def upload_file(room_id: str, file: UploadFile = File(...)):
    return load_sample("upload_file")

@router.get("/rooms/{room_id}/files")
def list_room_files(room_id: str):
    return load_sample("room_files")

@router.get("/rooms/{room_id}/students")
def list_room_students(room_id: str):
    return load_sample("room_students")

@router.post("/snap")
async def snap_and_ask(
    photo: UploadFile = File(...),
    room_id: str | None = Form(None),
):
    photo_bytes = await photo.read()
    return read_snap(photo_bytes)

@router.post("/copilot/message")
def copilot_message(request: CopilotRequest):
    return handle_message(request.room_id, request.text, request.file_id)