"""Climate and weather API endpoints"""

from datetime import date, timedelta
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_

from ..core.database import get_db
from ..models import ClimateData, WeatherForecast, Region

router = APIRouter()


@router.get("/regions")
async def list_regions(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """List all Saudi regions"""
    regions = db.query(Region).offset(skip).limit(limit).all()
    return {
        "total": db.query(Region).count(),
        "regions": regions
    }


@router.get("/regions/{region_id}")
async def get_region(region_id: int, db: Session = Depends(get_db)):
    """Get detailed information about a region"""
    region = db.query(Region).filter(Region.id == region_id).first()
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    return region


@router.get("/data")
async def get_climate_data(
    region_id: int,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    """Get historical climate data for a region"""
    if not start_date:
        start_date = date.today() - timedelta(days=30)
    if not end_date:
        end_date = date.today()

    data = db.query(ClimateData).filter(
        and_(
            ClimateData.region_id == region_id,
            ClimateData.date >= start_date,
            ClimateData.date <= end_date
        )
    ).order_by(ClimateData.date.desc()).all()

    return {
        "region_id": region_id,
        "start_date": start_date,
        "end_date": end_date,
        "data": data
    }


@router.get("/forecast")
async def get_weather_forecast(
    region_id: int,
    days: int = Query(7, ge=1, le=30),
    db: Session = Depends(get_db)
):
    """Get weather forecast for a region"""
    forecast_date = date.today()
    end_date = date.today() + timedelta(days=days)

    forecasts = db.query(WeatherForecast).filter(
        and_(
            WeatherForecast.region_id == region_id,
            WeatherForecast.forecast_for_date >= forecast_date,
            WeatherForecast.forecast_for_date <= end_date
        )
    ).order_by(WeatherForecast.forecast_for_date).all()

    return {
        "region_id": region_id,
        "forecast_from": forecast_date,
        "forecast_to": end_date,
        "forecasts": forecasts
    }


@router.get("/current/{region_id}")
async def get_current_conditions(region_id: int, db: Session = Depends(get_db)):
    """Get current weather conditions for a region"""
    today = date.today()

    # Get most recent climate data
    current = db.query(ClimateData).filter(
        and_(
            ClimateData.region_id == region_id,
            ClimateData.date <= today
        )
    ).order_by(ClimateData.date.desc()).first()

    if not current:
        raise HTTPException(
            status_code=404,
            detail="No current data available for this region"
        )

    return current
