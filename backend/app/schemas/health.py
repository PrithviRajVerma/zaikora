from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    success: bool = Field(default=True, description="Request status")
    message: str = Field(default="Zaikora API is running successfully.", description="Status message")
    environment: str = Field(description="Current deployment environment")
    timestamp: str = Field(description="ISO timestamp of the health check")
