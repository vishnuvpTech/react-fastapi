from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LOGIN_USERNAME_PASSWORD: bool = True
    LOGIN_OTP: bool = True
    LOGIN_MPN: bool = False   # you can toggle this anytime

    SECRET_KEY: str = "supersecret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
