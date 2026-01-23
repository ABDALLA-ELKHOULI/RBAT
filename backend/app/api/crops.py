"""Crops API endpoints"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_

from ..core.database import get_db
from ..models import Crop, CropSuitability, Region

router = APIRouter()


@router.get("/")
async def list_crops(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """List all crops with optional filtering"""
    query = db.query(Crop)

    if category:
        query = query.filter(Crop.category == category)

    if search:
        query = query.filter(
            or_(
                Crop.name_english.ilike(f"%{search}%"),
                Crop.name_arabic.like(f"%{search}%"),
                Crop.scientific_name.ilike(f"%{search}%")
            )
        )

    crops = query.offset(skip).limit(limit).all()
    return {
        "total": query.count(),
        "crops": crops
    }


@router.get("/{crop_id}")
async def get_crop(crop_id: int, db: Session = Depends(get_db)):
    """Get detailed information about a specific crop"""
    crop = db.query(Crop).filter(Crop.id == crop_id).first()
    if not crop:
        raise HTTPException(status_code=404, detail="Crop not found")
    return crop


@router.get("/{crop_id}/suitability")
async def get_crop_suitability(
    crop_id: int,
    region_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """Get crop suitability information for regions"""
    query = db.query(CropSuitability).filter(CropSuitability.crop_id == crop_id)

    if region_id:
        query = query.filter(CropSuitability.region_id == region_id)

    suitability = query.all()
    return {
        "crop_id": crop_id,
        "suitability": suitability
    }


@router.get("/categories/list")
async def list_categories(db: Session = Depends(get_db)):
    """List all crop categories"""
    categories = db.query(Crop.category).distinct().all()
    return {
        "categories": [cat[0] for cat in categories if cat[0]]
    }
