from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application configuration settings"""

    # Application
    APP_NAME: str = "RBAT - Research-Based Agriculture Technology"
    APP_VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "postgresql://rbat_user:rbat_password@localhost:5432/rbat_db"

    # AI Models
    ANTHROPIC_API_KEY: str
    OPENAI_API_KEY: Optional[str] = None
    CLAUDE_MODEL: str = "claude-sonnet-4-5-20250929"

    # Vector Database
    VECTOR_DIMENSIONS: int = 384  # sentence-transformers/all-MiniLM-L6-v2

    # External APIs
    OPENWEATHER_API_KEY: Optional[str] = None
    NASA_API_KEY: Optional[str] = None
    NEWS_API_KEY: Optional[str] = None

    # Saudi Arabia specific
    DEFAULT_COUNTRY: str = "SA"
    DEFAULT_TIMEZONE: str = "Asia/Riyadh"

    # Caching
    REDIS_URL: Optional[str] = "redis://localhost:6379"
    CACHE_TTL: int = 3600  # 1 hour

    # Security
    SECRET_KEY: str = "change-this-in-production-to-a-secure-random-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]

    # Data Collection
    DATA_COLLECTION_INTERVAL: int = 3600  # hourly
    MAX_ARTICLES_PER_SOURCE: int = 100

    # Forecasting
    FORECAST_PERIODS: int = 12  # months
    CONFIDENCE_INTERVAL: float = 0.95

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
