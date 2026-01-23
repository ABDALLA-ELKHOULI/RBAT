"""
Agriculture news collection from multiple sources
"""

import httpx
import feedparser
from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from sentence_transformers import SentenceTransformer

from ..app.core.config import settings
from ..app.models import NewsArticle


class NewsCollector:
    """Collect agriculture news from various sources"""

    def __init__(self):
        self.news_api_key = settings.NEWS_API_KEY
        self.embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

        # Agriculture news sources (RSS feeds)
        self.rss_feeds = [
            "https://www.farm-news.com/feed",
            "https://www.world-grain.com/rss",
            # Add Saudi-specific news sources
        ]

        # Search keywords for Saudi agriculture
        self.keywords = [
            "saudi agriculture",
            "saudi farming",
            "saudi livestock",
            "saudi fisheries",
            "middle east agriculture",
            "gulf agriculture"
        ]

    async def collect_from_newsapi(self, db: Session):
        """Collect from NewsAPI.org"""
        if not self.news_api_key:
            print("NewsAPI key not configured")
            return

        try:
            async with httpx.AsyncClient() as client:
                for keyword in self.keywords:
                    response = await client.get(
                        "https://newsapi.org/v2/everything",
                        params={
                            "q": keyword,
                            "apiKey": self.news_api_key,
                            "language": "en",
                            "sortBy": "publishedAt",
                            "pageSize": 10
                        }
                    )
                    response.raise_for_status()
                    data = response.json()

                    for article in data.get("articles", []):
                        await self._save_article(article, db)

            print("✓ Collected news from NewsAPI")

        except Exception as e:
            print(f"✗ Error collecting from NewsAPI: {e}")

    async def collect_from_rss(self, db: Session):
        """Collect from RSS feeds"""
        for feed_url in self.rss_feeds:
            try:
                feed = feedparser.parse(feed_url)

                for entry in feed.entries[:10]:  # Limit to 10 per feed
                    article = {
                        "title": entry.title,
                        "description": entry.get("summary", ""),
                        "url": entry.link,
                        "publishedAt": entry.get("published", datetime.now().isoformat()),
                        "source": {"name": feed.feed.title}
                    }
                    await self._save_article(article, db)

                print(f"✓ Collected from RSS: {feed.feed.title}")

            except Exception as e:
                print(f"✗ Error collecting from RSS {feed_url}: {e}")

    async def _save_article(self, article: dict, db: Session):
        """Save article to database"""
        try:
            # Check if article already exists
            existing = db.query(NewsArticle).filter(
                NewsArticle.url == article["url"]
            ).first()

            if existing:
                return  # Skip duplicates

            # Create embedding
            text_for_embedding = f"{article['title']} {article.get('description', '')}"
            embedding = self.embedding_model.encode(text_for_embedding)

            # Parse published date
            published_date = datetime.fromisoformat(
                article["publishedAt"].replace("Z", "+00:00")
            )

            # Determine category and relevance
            category, saudi_relevant = self._categorize_article(text_for_embedding)

            news_article = NewsArticle(
                title=article["title"],
                summary=article.get("description", ""),
                content=article.get("content", ""),
                source=article.get("source", {}).get("name", "Unknown"),
                author=article.get("author"),
                published_date=published_date,
                url=article["url"],
                category=category,
                saudi_relevant=1 if saudi_relevant else 0,
                embedding=embedding.tolist()
            )

            db.add(news_article)
            db.commit()

        except Exception as e:
            print(f"✗ Error saving article: {e}")
            db.rollback()

    def _categorize_article(self, text: str) -> tuple:
        """Categorize article and check Saudi relevance"""
        text_lower = text.lower()

        # Determine category
        if any(word in text_lower for word in ["market", "price", "trade", "export"]):
            category = "market"
        elif any(word in text_lower for word in ["policy", "regulation", "government"]):
            category = "policy"
        elif any(word in text_lower for word in ["technology", "innovation", "smart"]):
            category = "technology"
        elif any(word in text_lower for word in ["weather", "climate", "drought", "rain"]):
            category = "weather"
        elif any(word in text_lower for word in ["disease", "pest", "outbreak"]):
            category = "disease"
        else:
            category = "general"

        # Check Saudi relevance
        saudi_relevant = any(
            word in text_lower
            for word in ["saudi", "arabia", "ksa", "riyadh", "middle east", "gulf"]
        )

        return category, saudi_relevant


async def run_news_collection(db: Session):
    """Run news collection"""
    collector = NewsCollector()

    print("\n📰 Collecting agriculture news...")

    await collector.collect_from_newsapi(db)
    await collector.collect_from_rss(db)

    print("✓ News collection completed\n")
