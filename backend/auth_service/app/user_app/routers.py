from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    return [{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]

