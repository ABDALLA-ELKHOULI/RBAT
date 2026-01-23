"""Livestock API endpoints"""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_

from ..core.database import get_db
from ..models import Livestock, LivestockBreed

router = APIRouter()


@router.get("/")
async def list_livestock(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """List all livestock with optional filtering"""
    query = db.query(Livestock)

    if category:
        query = query.filter(Livestock.category == category)

    if search:
        query = query.filter(
            or_(
                Livestock.name_english.ilike(f"%{search}%"),
                Livestock.name_arabic.like(f"%{search}%")
            )
        )

    livestock = query.offset(skip).limit(limit).all()
    return {
        "total": query.count(),
        "livestock": livestock
    }


@router.get("/{livestock_id}")
async def get_livestock(livestock_id: int, db: Session = Depends(get_db)):
    """Get detailed information about specific livestock"""
    livestock = db.query(Livestock).filter(Livestock.id == livestock_id).first()
    if not livestock:
        raise HTTPException(status_code=404, detail="Livestock not found")
    return livestock


@router.get("/{livestock_id}/breeds")
async def get_livestock_breeds(livestock_id: int, db: Session = Depends(get_db)):
    """Get all breeds for specific livestock"""
    breeds = db.query(LivestockBreed).filter(
        LivestockBreed.livestock_id == livestock_id
    ).all()
    return {
        "livestock_id": livestock_id,
        "breeds": breeds
    }


@router.get("/categories/list")
async def list_categories(db: Session = Depends(get_db)):
    """List all livestock categories"""
    categories = db.query(Livestock.category).distinct().all()
    return {
        "categories": [cat[0] for cat in categories if cat[0]]
    }
