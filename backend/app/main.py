"""
RBAT - Research-Based Agriculture Technology
Main FastAPI application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .core.config import settings
from .core.database import init_db
from .api import crops, livestock, fisheries, climate, agent, reports

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Intelligent Agriculture Platform for Saudi Arabia",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_db()
    print(f"🌾 {settings.APP_NAME} v{settings.APP_VERSION} started!")
    print(f"📚 API Documentation: http://localhost:8000/docs")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "description": "Intelligent Agriculture Platform for Saudi Arabia",
        "status": "running",
        "endpoints": {
            "docs": "/docs",
            "api": settings.API_V1_PREFIX
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": settings.APP_VERSION
    }


# Include routers
app.include_router(
    crops.router,
    prefix=f"{settings.API_V1_PREFIX}/crops",
    tags=["Crops"]
)

app.include_router(
    livestock.router,
    prefix=f"{settings.API_V1_PREFIX}/livestock",
    tags=["Livestock"]
)

app.include_router(
    fisheries.router,
    prefix=f"{settings.API_V1_PREFIX}/fisheries",
    tags=["Fisheries"]
)

app.include_router(
    climate.router,
    prefix=f"{settings.API_V1_PREFIX}/climate",
    tags=["Climate & Weather"]
)

app.include_router(
    agent.router,
    prefix=f"{settings.API_V1_PREFIX}/agent",
    tags=["AI Agent"]
)

app.include_router(
    reports.router,
    prefix=f"{settings.API_V1_PREFIX}/reports",
    tags=["Reports"]
)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Handle all exceptions globally"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc) if settings.DEBUG else "An error occurred"
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
