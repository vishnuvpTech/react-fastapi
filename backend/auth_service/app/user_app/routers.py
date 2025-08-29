from fastapi import APIRouter, Depends, HTTPException
from app.user_app.config import settings
from app.user_app.service import login_with_password, login_with_otp, login_with_mpn

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login/password")
def login_password(username: str, password: str):
    if not settings.LOGIN_USERNAME_PASSWORD:
        raise HTTPException(status_code=403, detail="Password login disabled")
    return login_with_password(username, password)

@router.post("/login/otp")
def login_otp(phone: str, otp: str):
    if not settings.LOGIN_OTP:
        raise HTTPException(status_code=403, detail="OTP login disabled")
    return login_with_otp(phone, otp)

@router.post("/login/mpn")
def login_mpn(mpn: str):
    if not settings.LOGIN_MPN:
        raise HTTPException(status_code=403, detail="MPN login disabled")
    return login_with_mpn(mpn)
