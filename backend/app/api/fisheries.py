"""Fisheries API endpoints"""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_

from ..core.database import get_db
from ..models import Fishery, FishSpecies

router = APIRouter()


@router.get("/")
async def list_fisheries(
    skip: int = 0,
    limit: int = 100,
    type: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """List all fisheries with optional filtering"""
    query = db.query(Fishery)

    if type:
        query = query.filter(Fishery.type == type)

    if search:
        query = query.filter(
            or_(
                Fishery.name_english.ilike(f"%{search}%"),
                Fishery.name_arabic.like(f"%{search}%")
            )
        )

    fisheries = query.offset(skip).limit(limit).all()
    return {
        "total": query.count(),
        "fisheries": fisheries
    }


@router.get("/{fishery_id}")
async def get_fishery(fishery_id: int, db: Session = Depends(get_db)):
    """Get detailed information about specific fishery"""
    fishery = db.query(Fishery).filter(Fishery.id == fishery_id).first()
    if not fishery:
        raise HTTPException(status_code=404, detail="Fishery not found")
    return fishery


@router.get("/{fishery_id}/species")
async def get_fish_species(fishery_id: int, db: Session = Depends(get_db)):
    """Get all species for specific fishery"""
    species = db.query(FishSpecies).filter(
        FishSpecies.fishery_id == fishery_id
    ).all()
    return {
        "fishery_id": fishery_id,
        "species": species
    }


@router.get("/types/list")
async def list_types(db: Session = Depends(get_db)):
    """List all fishery types"""
    types = db.query(Fishery.type).distinct().all()
    return {
        "types": [t[0] for t in types if t[0]]
    }
