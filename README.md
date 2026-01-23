# 🌾 RBAT - Research-Based Agriculture Technology

**Intelligent Agriculture Platform for Saudi Arabia**

RBAT is an AI-powered agriculture intelligence platform that provides data-driven insights, forecasts, and recommendations for crops, livestock, fisheries, and climate across Saudi Arabia. Built for researchers, startups, students, and investors.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-green.svg)
![Node](https://img.shields.io/badge/node-18+-green.svg)
![Claude](https://img.shields.io/badge/AI-Claude%20Sonnet%204.5-purple.svg)

---

## ✨ Key Features

- 🤖 **AI Agent with Citations** - Ask any agriculture question, get answers with academic references
- 🌱 **Multi-Domain Coverage** - Crops, Livestock, Fisheries, Climate data
- 📊 **Market Forecasting** - Predict prices, yields, and trends
- 🗺️ **Regional Intelligence** - Specific insights for all Saudi regions
- 📈 **Report Generation** - Comprehensive research reports with references
- ⛅ **Weather Integration** - Real-time climate data and forecasts
- 📰 **News Aggregation** - Latest agriculture news and developments
- 🛰️ **Satellite Data** - Vegetation indices, soil moisture, crop health

---

## 🚀 Quick Start (5 Minutes)

### Prerequisites
- Docker & Docker Compose installed
- Anthropic API key (get from https://console.anthropic.com/)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ABDALLA-ELKHOULI/RBAT.git
cd RBAT

# 2. Configure environment
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# 3. Start the platform
docker-compose up

# 4. Open in browser
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/docs
```

**📘 For detailed instructions, see [GETTING_STARTED.md](GETTING_STARTED.md)**

---

## 💡 Usage Examples

### Chat with AI Agent

Visit **http://localhost:3000/chat** and ask:
- "What crops grow best in Riyadh during winter?"
- "Compare investment opportunities in date farming vs olive farming"
- "Forecast sheep prices for the next 6 months"
- "Generate a feasibility study for aquaculture in Eastern Province"

### Via API

```bash
curl -X POST http://localhost:8000/api/v1/agent/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What crops grow best in Riyadh?"}'
```

---

## 🛠️ Technology Stack

**Backend:** Python 3.11+ • FastAPI • PostgreSQL + pgvector • SQLAlchemy • Claude API

**Frontend:** Next.js 14 • React 18 • TypeScript • Tailwind CSS

**AI & Data:** Claude Sonnet 4.5 • RAG • Vector Search • OpenWeather • NewsAPI • NASA

**Infrastructure:** Docker • Cloud-ready (AWS, GCP, Azure)

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
