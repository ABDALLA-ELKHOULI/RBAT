"""
RAG (Retrieval-Augmented Generation) System for Agriculture Intelligence

This system retrieves relevant information from the database and external sources
to provide context for Claude AI to generate accurate, referenced responses.
"""

from typing import List, Dict, Any, Optional
from sentence_transformers import SentenceTransformer
import numpy as np
from sqlalchemy.orm import Session
from sqlalchemy import text

from ..core.config import settings
from ..models import (
    Crop, Livestock, Fishery, ClimateData,
    Reference, Region, NewsArticle
)


class RAGSystem:
    """Retrieval-Augmented Generation system for agriculture data"""

    def __init__(self):
        """Initialize RAG system with embedding model"""
        # Load embedding model (384 dimensions)
        self.embedding_model = SentenceTranser("sentence-transformers/all-MiniLM-L6-v2")

    def create_embedding(self, text: str) -> List[float]:
        """Create embedding vector from text"""
        embedding = self.embedding_model.encode(text)
        return embedding.tolist()

    async def retrieve_relevant_crops(
        self,
        query: str,
        db: Session,
        limit: int = 5,
        region_filter: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Retrieve relevant crop information based on query"""
        query_embedding = self.create_embedding(query)

        # Vector similarity search
        sql = text("""
            SELECT
                c.id, c.name_english, c.name_arabic, c.category,
                c.description, c.optimal_temperature, c.water_requirement,
                c.planting_season, c.harvest_season,
                c.average_yield_tons_per_hectare, c.market_price_sar_per_kg,
                1 - (c.embedding <=> :query_embedding::vector) as similarity
            FROM crops c
            WHERE c.embedding IS NOT NULL
            ORDER BY c.embedding <=> :query_embedding::vector
            LIMIT :limit
        """)

        result = db.execute(sql, {
            "query_embedding": str(query_embedding),
            "limit": limit
        })

        crops = []
        for row in result:
            crops.append({
                "id": row[0],
                "name": row[1],
                "name_arabic": row[2],
                "category": row[3],
                "description": row[4],
                "optimal_temperature": row[5],
                "water_requirement": row[6],
                "planting_season": row[7],
                "harvest_season": row[8],
                "yield": row[9],
                "price": row[10],
                "similarity": row[11]
            })

        return crops

    async def retrieve_relevant_livestock(
        self,
        query: str,
        db: Session,
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Retrieve relevant livestock information"""
        query_embedding = self.create_embedding(query)

        sql = text("""
            SELECT
                l.id, l.name_english, l.name_arabic, l.category,
                l.description, l.primary_purpose, l.heat_tolerance,
                l.water_requirement_liters_per_day, l.market_price_sar,
                1 - (l.embedding <=> :query_embedding::vector) as similarity
            FROM livestock l
            WHERE l.embedding IS NOT NULL
            ORDER BY l.embedding <=> :query_embedding::vector
            LIMIT :limit
        """)

        result = db.execute(sql, {
            "query_embedding": str(query_embedding),
            "limit": limit
        })

        livestock = []
        for row in result:
            livestock.append({
                "id": row[0],
                "name": row[1],
                "name_arabic": row[2],
                "category": row[3],
                "description": row[4],
                "purpose": row[5],
                "heat_tolerance": row[6],
                "water_requirement": row[7],
                "market_price": row[8],
                "similarity": row[9]
            })

        return livestock

    async def retrieve_relevant_fisheries(
        self,
        query: str,
        db: Session,
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Retrieve relevant fishery information"""
        query_embedding = self.create_embedding(query)

        sql = text("""
            SELECT
                f.id, f.name_english, f.name_arabic, f.type,
                f.description, f.production_method,
                f.optimal_temperature, f.market_price_sar_per_kg,
                1 - (f.embedding <=> :query_embedding::vector) as similarity
            FROM fisheries f
            WHERE f.embedding IS NOT NULL
            ORDER BY f.embedding <=> :query_embedding::vector
            LIMIT :limit
        """)

        result = db.execute(sql, {
            "query_embedding": str(query_embedding),
            "limit": limit
        })

        fisheries = []
        for row in result:
            fisheries.append({
                "id": row[0],
                "name": row[1],
                "name_arabic": row[2],
                "type": row[3],
                "description": row[4],
                "method": row[5],
                "temperature": row[6],
                "price": row[7],
                "similarity": row[8]
            })

        return fisheries

    async def retrieve_relevant_references(
        self,
        query: str,
        db: Session,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Retrieve relevant academic and source references"""
        query_embedding = self.create_embedding(query)

        sql = text("""
            SELECT
                r.id, r.title, r.authors, r.publication_year,
                r.source_type, r.publisher, r.url, r.doi,
                r.abstract, r.credibility_score, r.saudi_specific,
                1 - (r.embedding <=> :query_embedding::vector) as similarity
            FROM references r
            WHERE r.embedding IS NOT NULL
            ORDER BY r.embedding <=> :query_embedding::vector
            LIMIT :limit
        """)

        result = db.execute(sql, {
            "query_embedding": str(query_embedding),
            "limit": limit
        })

        references = []
        for row in result:
            references.append({
                "id": row[0],
                "title": row[1],
                "authors": row[2],
                "year": row[3],
                "type": row[4],
                "publisher": row[5],
                "url": row[6],
                "doi": row[7],
                "abstract": row[8],
                "credibility": row[9],
                "saudi_specific": bool(row[10]),
                "similarity": row[11]
            })

        return references

    async def retrieve_recent_news(
        self,
        query: str,
        db: Session,
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Retrieve recent relevant news articles"""
        query_embedding = self.create_embedding(query)

        sql = text("""
            SELECT
                n.id, n.title, n.summary, n.source,
                n.published_date, n.url, n.category, n.sentiment,
                1 - (n.embedding <=> :query_embedding::vector) as similarity
            FROM news_articles n
            WHERE n.embedding IS NOT NULL
            AND n.published_date >= CURRENT_DATE - INTERVAL '90 days'
            ORDER BY n.embedding <=> :query_embedding::vector
            LIMIT :limit
        """)

        result = db.execute(sql, {
            "query_embedding": str(query_embedding),
            "limit": limit
        })

        news = []
        for row in result:
            news.append({
                "id": row[0],
                "title": row[1],
                "summary": row[2],
                "source": row[3],
                "date": row[4],
                "url": row[5],
                "category": row[6],
                "sentiment": row[7],
                "similarity": row[8]
            })

        return news

    async def retrieve_climate_data(
        self,
        region_name: str,
        db: Session,
        days: int = 30
    ) -> Dict[str, Any]:
        """Retrieve recent climate data for a region"""
        # Get region
        region = db.query(Region).filter(
            (Region.name_english.ilike(f"%{region_name}%")) |
            (Region.name_arabic.like(f"%{region_name}%"))
        ).first()

        if not region:
            return {}

        # Get recent climate data
        sql = text("""
            SELECT
                date, temperature_avg, temperature_min, temperature_max,
                rainfall_mm, humidity_percentage, ndvi, soil_moisture
            FROM climate_data
            WHERE region_id = :region_id
            AND date >= CURRENT_DATE - INTERVAL ':days days'
            ORDER BY date DESC
        """)

        result = db.execute(sql, {"region_id": region.id, "days": days})

        climate_records = []
        for row in result:
            climate_records.append({
                "date": row[0],
                "temp_avg": row[1],
                "temp_min": row[2],
                "temp_max": row[3],
                "rainfall": row[4],
                "humidity": row[5],
                "ndvi": row[6],
                "soil_moisture": row[7]
            })

        return {
            "region": {
                "name": region.name_english,
                "name_arabic": region.name_arabic,
                "climate_zone": region.climate_zone
            },
            "data": climate_records
        }

    async def build_context(
        self,
        query: str,
        db: Session,
        include_crops: bool = True,
        include_livestock: bool = True,
        include_fisheries: bool = True,
        include_references: bool = True,
        include_news: bool = True
    ) -> Dict[str, Any]:
        """Build comprehensive context for AI agent"""
        context = {
            "query": query,
            "crops": [],
            "livestock": [],
            "fisheries": [],
            "references": [],
            "news": [],
            "climate": {}
        }

        if include_crops:
            context["crops"] = await self.retrieve_relevant_crops(query, db)

        if include_livestock:
            context["livestock"] = await self.retrieve_relevant_livestock(query, db)

        if include_fisheries:
            context["fisheries"] = await self.retrieve_relevant_fisheries(query, db)

        if include_references:
            context["references"] = await self.retrieve_relevant_references(query, db)

        if include_news:
            context["news"] = await self.retrieve_recent_news(query, db)

        return context

    def format_context_for_prompt(self, context: Dict[str, Any]) -> str:
        """Format retrieved context into a prompt for Claude"""
        prompt_parts = []

        prompt_parts.append("# Retrieved Context for Saudi Agriculture Query\n")

        # Crops
        if context.get("crops"):
            prompt_parts.append("\n## Relevant Crops:\n")
            for crop in context["crops"]:
                prompt_parts.append(f"""
**{crop['name']}** ({crop['name_arabic']})
- Category: {crop['category']}
- Description: {crop['description']}
- Optimal Temperature: {crop['optimal_temperature']}°C
- Water Requirement: {crop['water_requirement']}
- Planting Season: {crop['planting_season']}
- Average Yield: {crop['yield']} tons/hectare
- Market Price: {crop['price']} SAR/kg
- Relevance Score: {crop['similarity']:.2f}
""")

        # Livestock
        if context.get("livestock"):
            prompt_parts.append("\n## Relevant Livestock:\n")
            for animal in context["livestock"]:
                prompt_parts.append(f"""
**{animal['name']}** ({animal['name_arabic']})
- Category: {animal['category']}
- Purpose: {animal['purpose']}
- Heat Tolerance: {animal['heat_tolerance']}
- Water Requirement: {animal['water_requirement']} L/day
- Market Price: {animal['market_price']} SAR
- Relevance Score: {animal['similarity']:.2f}
""")

        # Fisheries
        if context.get("fisheries"):
            prompt_parts.append("\n## Relevant Fisheries:\n")
            for fish in context["fisheries"]:
                prompt_parts.append(f"""
**{fish['name']}** ({fish['name_arabic']})
- Type: {fish['type']}
- Production Method: {fish['method']}
- Optimal Temperature: {fish['temperature']}°C
- Market Price: {fish['price']} SAR/kg
- Relevance Score: {fish['similarity']:.2f}
""")

        # References
        if context.get("references"):
            prompt_parts.append("\n## Academic References:\n")
            for ref in context["references"][:5]:  # Top 5 references
                authors_str = ", ".join(ref['authors']) if ref['authors'] else "Unknown"
                prompt_parts.append(f"""
[{ref['id']}] {ref['title']} ({ref['year']})
- Authors: {authors_str}
- Source: {ref['type']} - {ref['publisher']}
- URL: {ref['url'] or ref['doi'] or 'N/A'}
- Saudi-specific: {'Yes' if ref['saudi_specific'] else 'No'}
- Credibility: {ref['credibility']}/100
""")

        # News
        if context.get("news"):
            prompt_parts.append("\n## Recent News:\n")
            for article in context["news"]:
                prompt_parts.append(f"""
**{article['title']}**
- Source: {article['source']}
- Date: {article['date']}
- Category: {article['category']}
- Summary: {article['summary']}
- URL: {article['url']}
""")

        return "\n".join(prompt_parts)
