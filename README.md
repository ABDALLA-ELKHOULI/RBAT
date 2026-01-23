# RBAT - Research-Based Agriculture Technology

An intelligent agriculture platform for Saudi Arabia providing data-driven insights for crops, livestock, fisheries, and climate with comprehensive references and forecasting capabilities.

## Overview

RBAT is designed for researchers, startups, students, and investment arms who need access to reliable agricultural data and intelligence for Saudi Arabia.

### Key Features

- **Multi-Domain Intelligence**: Crops, Livestock, Fisheries, Climate
- **Data Aggregation**: Weather, soil, satellite imagery, market news
- **AI-Powered Insights**: Intelligent agent using Claude API with RAG
- **Forecasting**: Predictive analytics for agricultural planning
- **Referenced Data**: All insights backed by verified sources
- **Interactive Reports**: Generate comprehensive reports with citations
- **Crop Recommendations**: Where to grow what, based on climate, soil, water availability

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Next.js Frontend                      │
│          (Interactive Dashboard & Reports)               │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                  FastAPI Backend                         │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   AI Agent   │  │ Data Pipeline│  │  Analytics   │  │
│  │ Claude + RAG │  │  Collection  │  │ & Forecasting│  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│         PostgreSQL + pgvector (Vector DB)                │
│   Crops │ Livestock │ Fisheries │ Climate │ References  │
└─────────────────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              External Data Sources                       │
│  Weather APIs │ Satellite │ News │ Agricultural DBs     │
└─────────────────────────────────────────────────────────┘
```

## Project Structure

```
RBAT/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── agents/         # AI agent logic
│   │   ├── services/       # Business logic
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic schemas
│   │   └── core/           # Config, dependencies
│   ├── data_pipeline/      # Data collection scripts
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/               # Next.js frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Next.js pages
│   │   ├── services/      # API clients
│   │   └── utils/         # Utilities
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml      # Local development
├── deployment/             # Cloud deployment configs
└── docs/                   # Documentation
```

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+ (for local frontend dev)
- Python 3.11+ (for local backend dev)
- Anthropic API key (for Claude AI)

### Environment Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and configure:
   - `ANTHROPIC_API_KEY`: Your Claude API key
   - `DATABASE_URL`: PostgreSQL connection
   - External API keys (weather, satellite, etc.)

### Run with Docker

```bash
docker-compose up
```

- Backend API: http://localhost:8000
- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs

## Features in Detail

### 1. Intelligent Agent
- Powered by Claude with RAG (Retrieval-Augmented Generation)
- Answers questions about Saudi agriculture
- Provides recommendations with citations
- Multi-domain knowledge: crops, livestock, fisheries, climate

### 2. Data Collection
- Automated collection from multiple sources
- Real-time weather and climate data
- Satellite imagery analysis
- Agricultural news and market indicators
- Soil composition databases
- Water availability metrics

### 3. Analytics & Forecasting
- Time-series forecasting for yields, prices, climate
- Crop suitability analysis
- Risk assessment
- Market trend analysis

### 4. Report Generation
- Comprehensive reports with visualizations
- All data points include references
- Export to PDF, Excel, JSON
- Customizable templates

## Data Domains

### Crops
- Suitable crops for different regions in Saudi Arabia
- Planting seasons and calendars
- Water requirements
- Expected yields
- Market prices and trends

### Livestock
- Breed recommendations
- Feed requirements
- Disease management
- Market analysis

### Fisheries
- Aquaculture potential
- Fish species by region
- Water quality requirements
- Production forecasts

### Climate & Environment
- Temperature, rainfall, humidity patterns
- Soil composition by region
- Water availability and irrigation
- Satellite vegetation indices (NDVI)
- Weather forecasts

## API Endpoints

- `POST /api/v1/query` - Ask the AI agent anything
- `GET /api/v1/crops` - List crops data
- `GET /api/v1/crops/{id}` - Crop details
- `POST /api/v1/forecast` - Generate forecasts
- `POST /api/v1/reports` - Create reports
- `GET /api/v1/regions` - Saudi regions data
- `GET /api/v1/weather` - Weather data

## Cloud Deployment

Supports deployment to:
- **AWS**: ECS, RDS, S3
- **Google Cloud**: Cloud Run, Cloud SQL
- **Azure**: Container Apps, PostgreSQL

See `deployment/` directory for platform-specific guides.

## Contributing

This is a specialized platform for Saudi Arabian agriculture. Contributions welcome!

## License

MIT License

## Support

For issues and questions, please open a GitHub issue.
