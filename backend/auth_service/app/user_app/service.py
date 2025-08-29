from fastapi import HTTPException
from app.user_app.utils.jwt_handler import create_access_token
from app.user_app.utils.password_utils import verify_password

# Mock user
USERS = {
    "john": {"password": "hashed123", "phone": "+911234567890"}
}

def login_with_password(username: str, password: str):
    user = USERS.get(username)
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}

def login_with_otp(phone: str, otp: str):
    # Validate OTP from DB/Redis
    if otp != "123456":
        raise HTTPException(status_code=401, detail="Invalid OTP")
    token = create_access_token({"sub": phone})
    return {"access_token": token, "token_type": "bearer"}

def login_with_mpn(mpn: str):
    # Implement MPN-based validation (could be from telco API or DB)
    if mpn != "MPN-VALID":
        raise HTTPException(status_code=401, detail="Invalid MPN")
    token = create_access_token({"sub": mpn})
    return {"access_token": token, "token_type": "bearer"}
