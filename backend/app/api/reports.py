"""Reports API endpoints"""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..agents import AgricultureAgent

router = APIRouter()
agent = AgricultureAgent()


class ReportGenerationRequest(BaseModel):
    """Request model for report generation"""
    title: str
    topic: str
    region: Optional[str] = None
    include_crops: bool = True
    include_livestock: bool = True
    include_fisheries: bool = True
    include_climate: bool = True
    include_market_analysis: bool = True
    include_forecasts: bool = True
    format: str = "json"  # json, pdf, excel


@router.post("/generate")
async def generate_comprehensive_report(
    request: ReportGenerationRequest,
    db: Session = Depends(get_db)
):
    """
    Generate a comprehensive agriculture report

    Includes:
    - Executive summary
    - Data analysis with charts
    - Market insights
    - Forecasts and projections
    - Recommendations
    - Full citations and references

    Outputs: JSON, PDF, or Excel
    """
    try:
        result = await agent.generate_report(
            request.topic,
            request.region,
            db
        )

        # Add report metadata
        report = {
            "title": request.title,
            "topic": request.topic,
            "region": request.region or "All Saudi Arabia",
            "generated_at": "now",  # Will be replaced with actual timestamp
            "format": request.format,
            "content": result["response"],
            "references": result["references"],
            "metadata": {
                "ai_model": result["model"],
                "data_sources": result["context_used"]
            }
        }

        # For now, return JSON
        # TODO: Implement PDF and Excel generation
        if request.format == "pdf":
            return {"message": "PDF generation coming soon", "report": report}
        elif request.format == "excel":
            return {"message": "Excel generation coming soon", "report": report}
        else:
            return report

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/templates")
async def list_report_templates():
    """List available report templates"""
    return {
        "templates": [
            {
                "id": "crop_analysis",
                "name": "Crop Analysis Report",
                "description": "Comprehensive analysis of specific crops"
            },
            {
                "id": "regional_overview",
                "name": "Regional Agriculture Overview",
                "description": "Complete overview of agriculture in a region"
            },
            {
                "id": "investment_opportunity",
                "name": "Investment Opportunity Report",
                "description": "Analysis for investment decisions"
            },
            {
                "id": "market_forecast",
                "name": "Market Forecast Report",
                "description": "Market trends and price forecasts"
            },
            {
                "id": "feasibility_study",
                "name": "Feasibility Study",
                "description": "Project feasibility analysis"
            }
        ]
    }
