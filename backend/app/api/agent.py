"""
AI Agent API endpoints
"""

from typing import Optional, List, Dict
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..agents import AgricultureAgent


router = APIRouter()
agent = AgricultureAgent()


class QueryRequest(BaseModel):
    """Request model for agent queries"""
    query: str
    conversation_history: Optional[List[Dict[str, str]]] = None


class CropRecommendationRequest(BaseModel):
    """Request model for crop recommendations"""
    region: str
    season: Optional[str] = None
    water_availability: Optional[str] = None
    budget_sar: Optional[float] = None


class LivestockAnalysisRequest(BaseModel):
    """Request model for livestock analysis"""
    region: str
    livestock_type: Optional[str] = None
    investment_amount: Optional[float] = None


class MarketForecastRequest(BaseModel):
    """Request model for market forecasts"""
    product: str
    months_ahead: int = 6


class ReportRequest(BaseModel):
    """Request model for report generation"""
    topic: str
    region: Optional[str] = None


class WeatherAdvisoryRequest(BaseModel):
    """Request model for weather advisory"""
    region: str
    days_ahead: int = 7


class ChatRequest(BaseModel):
    """Request model for chat"""
    message: str
    conversation_history: List[Dict[str, str]] = []


@router.post("/query")
async def query_agent(
    request: QueryRequest,
    db: Session = Depends(get_db)
):
    """
    Query the AI agent with any agriculture-related question

    The agent will:
    - Retrieve relevant data from the database
    - Use Claude AI to generate intelligent responses
    - Provide references and citations
    """
    try:
        result = await agent.query(
            request.query,
            db,
            request.conversation_history
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/recommend-crops")
async def recommend_crops(
    request: CropRecommendationRequest,
    db: Session = Depends(get_db)
):
    """
    Get crop recommendations for specific conditions

    Provides:
    - Suitable crops for the region
    - Yield estimates
    - Cost analysis
    - ROI projections
    - Planting calendars
    """
    try:
        result = await agent.recommend_crops(
            request.region,
            request.season,
            request.water_availability,
            request.budget_sar,
            db
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze-livestock")
async def analyze_livestock(
    request: LivestockAnalysisRequest,
    db: Session = Depends(get_db)
):
    """
    Analyze livestock farming opportunities

    Provides:
    - Suitable breeds for the region
    - Investment requirements
    - Operating costs
    - Revenue projections
    - Risk analysis
    """
    try:
        result = await agent.analyze_livestock_opportunity(
            request.region,
            request.livestock_type,
            request.investment_amount,
            db
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/forecast-market")
async def forecast_market(
    request: MarketForecastRequest,
    db: Session = Depends(get_db)
):
    """
    Forecast market conditions for agricultural products

    Provides:
    - Price trend analysis
    - Supply and demand forecasts
    - Market influencing factors
    - Investment timing recommendations
    """
    try:
        result = await agent.forecast_market(
            request.product,
            request.months_ahead,
            db
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate-report")
async def generate_report(
    request: ReportRequest,
    db: Session = Depends(get_db)
):
    """
    Generate comprehensive research reports

    Creates detailed reports with:
    - Executive summary
    - Data analysis
    - Market insights
    - Forecasts
    - Recommendations
    - Full references
    """
    try:
        result = await agent.generate_report(
            request.topic,
            request.region,
            db
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/weather-advisory")
async def weather_advisory(
    request: WeatherAdvisoryRequest,
    db: Session = Depends(get_db)
):
    """
    Get agricultural advisory based on weather forecast

    Provides:
    - Activity recommendations
    - Irrigation advice
    - Risk alerts
    - Optimal timing for operations
    """
    try:
        result = await agent.get_weather_agriculture_advisory(
            request.region,
            request.days_ahead,
            db
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/chat")
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    """
    Interactive chat with the agriculture AI agent

    Maintains conversation context for natural dialogue
    """
    try:
        result = await agent.chat(
            request.message,
            request.conversation_history,
            db
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
