"""
Agriculture Intelligence Agent

Uses Claude AI with RAG to provide intelligent insights about Saudi agriculture
with comprehensive references and citations.
"""

from typing import Dict, Any, List, Optional
from anthropic import Anthropic
from sqlalchemy.orm import Session

from ..core.config import settings
from .rag_system import RAGSystem


class AgricultureAgent:
    """Intelligent agriculture agent for Saudi Arabia"""

    def __init__(self):
        """Initialize agent with Claude client and RAG system"""
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.rag_system = RAGSystem()
        self.model = settings.CLAUDE_MODEL

    def _create_system_prompt(self) -> str:
        """Create system prompt for the agriculture agent"""
        return """You are an expert agricultural consultant specializing in Saudi Arabian agriculture.

Your role is to provide:
1. **Data-driven insights** about crops, livestock, fisheries, and climate
2. **Evidence-based recommendations** for farming, investment, and research
3. **Comprehensive references** for all information provided
4. **Forecasts and predictions** based on available data
5. **Regional specificity** tailored to Saudi Arabian conditions

Key principles:
- Always cite your sources using the reference IDs provided in [brackets]
- Be specific about Saudi Arabian regions, climate zones, and conditions
- Consider water scarcity, heat tolerance, and desert climate in recommendations
- Provide practical, actionable advice
- Include economic data (costs, yields, ROI) when available
- Acknowledge limitations and uncertainties
- Prioritize recent data and Saudi-specific research

Target audiences:
- Researchers conducting agricultural studies
- Startups building agriculture businesses
- Students learning about Saudi agriculture
- Investment arms evaluating agriculture opportunities
- Farmers planning their crops and livestock

When providing recommendations:
- Specify which regions are suitable
- Include planting/raising timelines
- Estimate costs and returns
- List water and resource requirements
- Mention risks and challenges
- Suggest mitigation strategies

Always structure responses with:
1. Direct answer to the question
2. Supporting data and evidence
3. Regional considerations
4. Economic analysis
5. References and sources
"""

    def _create_user_prompt(self, query: str, context: str) -> str:
        """Create user prompt with query and retrieved context"""
        return f"""{context}

---

## User Question:
{query}

## Instructions:
Using the retrieved context above, provide a comprehensive answer that:
1. Directly addresses the user's question
2. Incorporates relevant data from crops, livestock, fisheries, climate, and news
3. Cites all sources using reference IDs [number]
4. Provides specific recommendations for Saudi Arabia
5. Includes practical next steps or actionable advice

If the context doesn't contain enough information, acknowledge this and provide general guidance based on your knowledge of Saudi agriculture, but clearly distinguish between referenced facts and general knowledge.
"""

    async def query(
        self,
        user_query: str,
        db: Session,
        conversation_history: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        Process a user query and return an intelligent response

        Args:
            user_query: The user's question or request
            db: Database session
            conversation_history: Optional previous conversation for context

        Returns:
            Dict containing response, references, and metadata
        """
        # Build context using RAG
        context = await self.rag_system.build_context(user_query, db)
        formatted_context = self.rag_system.format_context_for_prompt(context)

        # Prepare messages
        messages = []

        # Add conversation history if provided
        if conversation_history:
            messages.extend(conversation_history)

        # Add current query
        user_prompt = self._create_user_prompt(user_query, formatted_context)
        messages.append({
            "role": "user",
            "content": user_prompt
        })

        # Call Claude API
        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=self._create_system_prompt(),
            messages=messages
        )

        # Extract response text
        response_text = response.content[0].text

        # Return structured response
        return {
            "response": response_text,
            "references": context.get("references", []),
            "context_used": {
                "crops_count": len(context.get("crops", [])),
                "livestock_count": len(context.get("livestock", [])),
                "fisheries_count": len(context.get("fisheries", [])),
                "references_count": len(context.get("references", [])),
                "news_count": len(context.get("news", []))
            },
            "model": self.model,
            "usage": {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens
            }
        }

    async def recommend_crops(
        self,
        region: str,
        season: Optional[str],
        water_availability: Optional[str],
        budget_sar: Optional[float],
        db: Session
    ) -> Dict[str, Any]:
        """
        Recommend suitable crops for specific conditions

        Args:
            region: Saudi region name
            season: Planting season
            water_availability: Water availability level
            budget_sar: Budget in Saudi Riyals
            db: Database session

        Returns:
            Crop recommendations with detailed analysis
        """
        query = f"""What crops should I grow in {region}, Saudi Arabia?
        - Season: {season or 'any'}
        - Water availability: {water_availability or 'moderate'}
        - Budget: {budget_sar or 'flexible'} SAR

        Please provide specific crop recommendations with yield estimates, costs, and ROI."""

        return await self.query(query, db)

    async def analyze_livestock_opportunity(
        self,
        region: str,
        livestock_type: Optional[str],
        investment_amount: Optional[float],
        db: Session
    ) -> Dict[str, Any]:
        """Analyze livestock farming opportunities"""
        query = f"""I want to start a livestock farm in {region}, Saudi Arabia.
        - Livestock type: {livestock_type or 'open to suggestions'}
        - Investment budget: {investment_amount or 'flexible'} SAR

        Please analyze the opportunity, recommend suitable breeds, estimate costs, and project returns."""

        return await self.query(query, db)

    async def forecast_market(
        self,
        product: str,
        months_ahead: int,
        db: Session
    ) -> Dict[str, Any]:
        """Forecast market conditions for agricultural products"""
        query = f"""Forecast the market conditions for {product} in Saudi Arabia for the next {months_ahead} months.

        Include:
        - Price trends
        - Supply and demand analysis
        - External factors (weather, policy, imports)
        - Investment recommendations"""

        return await self.query(query, db)

    async def generate_report(
        self,
        topic: str,
        region: Optional[str],
        db: Session
    ) -> Dict[str, Any]:
        """Generate a comprehensive report on an agriculture topic"""
        query = f"""Generate a comprehensive research report on: {topic}
        {"Region focus: " + region if region else "Region: All of Saudi Arabia"}

        The report should include:
        1. Executive Summary
        2. Current State Analysis
        3. Data and Statistics (with references)
        4. Market Analysis
        5. Opportunities and Challenges
        6. Forecasts and Projections
        7. Recommendations
        8. References

        Make it suitable for researchers, investors, and policymakers."""

        return await self.query(query, db)

    async def get_weather_agriculture_advisory(
        self,
        region: str,
        days_ahead: int,
        db: Session
    ) -> Dict[str, Any]:
        """Provide agricultural advisory based on weather forecast"""
        # First get climate data
        climate_data = await self.rag_system.retrieve_climate_data(region, db)

        query = f"""Based on the recent climate data for {region}, provide agricultural advisory for the next {days_ahead} days.

        Include:
        - What crops/activities are suitable now
        - What to avoid
        - Irrigation recommendations
        - Pest and disease risks
        - Optimal farming activities"""

        return await self.query(query, db)

    async def chat(
        self,
        message: str,
        conversation_history: List[Dict[str, str]],
        db: Session
    ) -> Dict[str, Any]:
        """
        Interactive chat interface

        Args:
            message: User's message
            conversation_history: Previous conversation messages
            db: Database session

        Returns:
            Agent response with updated conversation
        """
        result = await self.query(message, db, conversation_history)

        # Update conversation history
        updated_history = conversation_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": result["response"]}
        ]

        result["conversation_history"] = updated_history
        return result
