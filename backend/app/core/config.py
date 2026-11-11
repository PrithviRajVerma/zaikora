from pathlib import Path
from typing import List
from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    PROJECT_NAME: str = "Zaikora API"
    PORT: int = Field(default=5000, validation_alias="PORT")
    NODE_ENV: str = Field(default="development", validation_alias="NODE_ENV")
    CLIENT_URL: str = Field(default="http://localhost:5173", validation_alias="CLIENT_URL")
    
    MONGO_URI: str = Field(default="", validation_alias="MONGO_URI")
    JWT_SECRET: str = Field(default="your_jwt_secret", validation_alias="JWT_SECRET")
    
    RAZORPAY_KEY_ID: str = Field(default="", validation_alias="RAZORPAY_KEY_ID")
    RAZORPAY_KEY_SECRET: str = Field(default="", validation_alias="RAZORPAY_KEY_SECRET")
    
    CLOUDINARY_CLOUD_NAME: str = Field(default="", validation_alias="CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY: str = Field(default="", validation_alias="CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET: str = Field(default="", validation_alias="CLOUDINARY_API_SECRET")
    
    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / ".env", ".env", "backend/.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @computed_field
    @property
    def is_production(self) -> bool:
        return self.NODE_ENV.lower() == "production"

    @computed_field
    @property
    def cors_origins(self) -> List[str]:
        origins = [origin.strip() for origin in self.CLIENT_URL.split(",") if origin.strip()]
        if not origins:
            origins = ["http://localhost:5173"]
        return origins

settings = Settings()
