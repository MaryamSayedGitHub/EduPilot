from fastapi import APIRouter

router = APIRouter(tags=["M1 platform"])

# Temporary: one demo account. Replaced with a real database check later.
DEMO_USER = {"token": "demo-token-sara-123", "user_id": "u_sara", "name": "سارة أحمد", "role": "student"}


@router.post("/auth/login")
def login(body: dict):
    return DEMO_USER