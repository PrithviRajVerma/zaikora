from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings
from app.core.logger import logger


class DatabaseManager:
    client: Optional[AsyncIOMotorClient] = None
    db: Optional[AsyncIOMotorDatabase] = None


db_manager = DatabaseManager()


async def connect_to_mongo() -> None:
    if not settings.MONGO_URI:
        logger.warning("MONGO_URI is not set. MongoDB client initialization skipped.")
        return

    try:
        logger.info("Connecting to MongoDB...")
        db_manager.client = AsyncIOMotorClient(
            settings.MONGO_URI,
            serverSelectionTimeoutMS=5000,
        )
        # Verify connection
        await db_manager.client.admin.command("ping")

        default_db = db_manager.client.get_default_database()
        db_manager.db = default_db if default_db is not None else db_manager.client["zaikora"]

        logger.info("MongoDB connected successfully.")
    except Exception as e:
        logger.error(f"MongoDB connection failed: {e}")
        if settings.is_production:
            raise e
        logger.warning("Continuing in development mode. Ensure MONGO_URI is valid to use database features.")


async def close_mongo_connection() -> None:
    if db_manager.client:
        logger.info("Closing MongoDB connection...")
        db_manager.client.close()
        logger.info("MongoDB connection closed.")


def get_database() -> AsyncIOMotorDatabase:
    if db_manager.db is None:
        raise RuntimeError("Database is not initialized or connected.")
    return db_manager.db
