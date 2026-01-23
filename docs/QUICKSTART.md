# RBAT Quick Start Guide

Get RBAT up and running in minutes!

## Overview

RBAT (Research-Based Agriculture Technology) is an intelligent agriculture platform for Saudi Arabia that provides:

- 🌱 Crop recommendations and data
- 🐄 Livestock information and analysis
- 🐟 Fisheries and aquaculture insights
- 🌤️ Climate data and weather forecasts
- 🤖 AI-powered agent with comprehensive references
- 📊 Report generation and forecasting

## Prerequisites

You need:
- Docker and Docker Compose
- Anthropic API key (get it from https://console.anthropic.com/)
- (Optional) OpenWeather API key for weather data
- (Optional) NewsAPI key for news aggregation

## Installation

### Step 1: Get the API Key

1. Go to https://console.anthropic.com/
2. Create an account or sign in
3. Navigate to API Keys
4. Create a new API key
5. Copy the key (starts with `sk-ant-`)

### Step 2: Clone and Configure

```bash
# Clone the repository
git clone <your-repo-url>
cd RBAT

# Copy environment file
cp .env.example .env

# Edit .env and add your API key
nano .env  # or use any text editor
```

In `.env`, set:
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

### Step 3: Start Everything

```bash
# Start all services with Docker Compose
docker-compose up

# Or run in background
docker-compose up -d
```

Wait a minute for all services to start. You'll see:
```
✓ Container rbat-db-1        Started
✓ Container rbat-redis-1     Started
✓ Container rbat-backend-1   Started
✓ Container rbat-frontend-1  Started
```

### Step 4: Access the Application

Open your browser and visit:

- **Frontend (Main App):** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs

## First Steps

### 1. Explore the AI Agent

1. Go to http://localhost:3000/chat
2. Ask questions like:
   - "What crops grow best in Riyadh region?"
   - "Recommend livestock for Al-Jouf"
   - "What are the best aquaculture opportunities in Saudi Arabia?"
   - "Forecast wheat prices for the next 6 months"

### 2. Browse Data

- **Crops:** http://localhost:3000/crops
- **Livestock:** http://localhost:3000/livestock
- **Fisheries:** http://localhost:3000/fisheries
- **Climate:** http://localhost:3000/climate

### 3. Generate Reports

1. Go to http://localhost:3000/reports
2. Choose a template or create custom report
3. Specify region and topic
4. Get comprehensive report with references

### 4. Use the API

Try the API directly:

```bash
# Query the AI agent
curl -X POST http://localhost:8000/api/v1/agent/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are the best crops for Riyadh?"
  }'

# Get crop recommendations
curl -X POST http://localhost:8000/api/v1/agent/recommend-crops \
  -H "Content-Type: application/json" \
  -d '{
    "region": "Riyadh",
    "season": "winter",
    "water_availability": "moderate",
    "budget_sar": 50000
  }'

# List all crops
curl http://localhost:8000/api/v1/crops

# Get weather forecast
curl "http://localhost:8000/api/v1/climate/forecast?region_id=1&days=7"
```

## Adding Data

### Load Sample Data

Currently, the database is empty. You'll need to load sample data:

```bash
# Access the backend container
docker exec -it rbat-backend-1 bash

# Initialize database
python -c "from app.core.database import init_db; init_db()"

# Load sample data (you'll need to create these scripts)
# python scripts/load_sample_data.py
```

### Add Your Own Data

You can add data via:
1. Direct database access
2. Admin API endpoints (to be implemented)
3. CSV imports (to be implemented)

## Collecting External Data

To enable automatic data collection from external sources:

### Weather Data

1. Get OpenWeather API key: https://openweathermap.org/api
2. Add to `.env`:
   ```
   OPENWEATHER_API_KEY=your_key_here
   ```
3. Run collector:
   ```bash
   docker exec rbat-backend-1 python -m backend.data_pipeline.weather_collector
   ```

### News Data

1. Get NewsAPI key: https://newsapi.org
2. Add to `.env`:
   ```
   NEWS_API_KEY=your_key_here
   ```
3. Run collector:
   ```bash
   docker exec rbat-backend-1 python -m backend.data_pipeline.news_collector
   ```

## Common Tasks

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Restart Services

```bash
# Restart everything
docker-compose restart

# Restart specific service
docker-compose restart backend
```

### Stop Everything

```bash
docker-compose down

# Stop and remove volumes (clears database)
docker-compose down -v
```

### Update Code

```bash
# Pull latest changes
git pull

# Rebuild containers
docker-compose up --build
```

## Architecture Overview

```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │
┌──────▼──────────┐
│  Next.js (3000) │  Frontend
└──────┬──────────┘
       │
┌──────▼──────────┐
│  FastAPI (8000) │  Backend API + AI Agent
└──────┬──────────┘
       │
┌──────▼──────────┐
│  PostgreSQL     │  Database + Vector DB
│  + pgvector     │
└─────────────────┘
```

## Troubleshooting

### Port Already in Use

If ports 3000, 5432, or 8000 are in use:

```bash
# Find and kill process using port 3000
lsof -ti:3000 | xargs kill -9

# Or change ports in docker-compose.yml
```

### Database Connection Error

```bash
# Check if database is running
docker-compose ps

# Check database logs
docker-compose logs db

# Verify pgvector extension
docker exec rbat-db-1 psql -U rbat_user -d rbat_db -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

### Frontend Can't Connect to Backend

Check `NEXT_PUBLIC_API_URL` in `.env`:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Rebuild frontend:
```bash
docker-compose up --build frontend
```

### AI Agent Returns Errors

1. Verify API key is correct in `.env`
2. Check you have API credits: https://console.anthropic.com/
3. Review backend logs: `docker-compose logs backend`

## Next Steps

1. **Add Your Data:** Import crops, livestock, and fishery data for Saudi Arabia
2. **Configure APIs:** Set up weather, satellite, and news APIs
3. **Customize:** Modify prompts, add features, adjust UI
4. **Deploy:** Follow deployment guide for production
5. **Scale:** Add caching, load balancing, monitoring

## Resources

- **Full Documentation:** See `/docs` directory
- **API Documentation:** http://localhost:8000/docs
- **Deployment Guide:** `docs/DEPLOYMENT.md`
- **API Reference:** `docs/API.md`

## Getting Help

If you encounter issues:

1. Check logs: `docker-compose logs`
2. Review documentation in `/docs`
3. Check API docs: http://localhost:8000/docs
4. Open GitHub issue with details

## Sample Questions for AI Agent

Try asking:

**Crops:**
- "What vegetables can I grow in Riyadh during winter?"
- "Compare date palm and olive cultivation in Al-Ahsa"
- "What are the water requirements for wheat in Saudi Arabia?"

**Livestock:**
- "What sheep breeds are best for the Northern Border region?"
- "Analyze the profitability of camel farming in Al-Qassim"
- "Compare dairy cattle vs meat cattle for Riyadh region"

**Fisheries:**
- "What are the best fish species for aquaculture in Eastern Province?"
- "Analyze shrimp farming opportunities in the Red Sea coast"

**Market & Investment:**
- "Forecast tomato prices for the next 6 months"
- "What are the best agricultural investment opportunities in Jizan?"
- "Generate a feasibility study for organic farming in Taif"

**Climate:**
- "What are the climate challenges for agriculture in Najran?"
- "When is the best time to plant wheat in Hail?"

## License

MIT License - see LICENSE file for details
