# 🚀 Getting Started with RBAT

## What You'll Need (Prerequisites)

1. **Computer with:**
   - Docker installed ([Install Docker](https://docs.docker.com/get-docker/))
   - Git installed
   - 4GB+ RAM available

2. **API Keys (Get these first):**
   - **Anthropic API Key** (REQUIRED) - Get from https://console.anthropic.com/
     - Sign up for an account
     - Go to API Keys section
     - Create a new key
     - Copy it somewhere safe

   - **OpenWeather API Key** (Optional but recommended) - Get from https://openweathermap.org/api
     - Free tier: 1,000 calls/day

   - **NewsAPI Key** (Optional) - Get from https://newsapi.org
     - Free tier: 100 requests/day

   - **NASA API Key** (Optional) - Get from https://api.nasa.gov
     - Free, instant approval

---

## 🎯 Option 1: Quick Start (5 Minutes)

This gets you running immediately with Docker.

### Step 1: Clone the Repository

```bash
git clone https://github.com/ABDALLA-ELKHOULI/RBAT.git
cd RBAT
```

### Step 2: Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your favorite editor
nano .env
# or
vim .env
# or use any text editor
```

**Add your API keys to .env:**
```bash
# REQUIRED - Get from https://console.anthropic.com/
ANTHROPIC_API_KEY=sk-ant-your-key-here

# OPTIONAL but recommended
OPENWEATHER_API_KEY=your_openweather_key_here
NEWS_API_KEY=your_newsapi_key_here
NASA_API_KEY=your_nasa_key_here
```

### Step 3: Start Everything

```bash
# This will download and start all services
docker-compose up
```

**Wait for the message:** `Application startup complete`

### Step 4: Open Your Browser

- **Main App:** http://localhost:3000
- **API Docs:** http://localhost:8000/docs
- **Chat Interface:** http://localhost:3000/chat

That's it! You're running!

---

## 🎯 Option 2: Manual Setup (More Control)

If you prefer to run services individually or don't use Docker:

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export ANTHROPIC_API_KEY=your_key_here
export DATABASE_URL=postgresql://user:pass@localhost:5432/rbat_db

# Run database migrations (first time only)
alembic upgrade head

# Start the backend server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
# Open a new terminal
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Database Setup (PostgreSQL)

```bash
# Install PostgreSQL with pgvector extension
# On Ubuntu:
sudo apt-get install postgresql postgresql-contrib

# Create database
sudo -u postgres createdb rbat_db

# Install pgvector extension
sudo -u postgres psql rbat_db -c "CREATE EXTENSION vector;"
```

---

## 📱 How to Use the Platform

### 1. Chat with the AI Agent

**Web Interface:**
1. Go to http://localhost:3000/chat
2. Type your question in the chat box
3. Get intelligent responses with citations

**Example Questions:**
```
"What crops grow best in Riyadh during winter?"
"I have 100,000 SAR to invest in livestock in Al-Jouf. What do you recommend?"
"Generate a market forecast for wheat prices over the next 6 months"
"What are the water requirements for date palm cultivation?"
```

**Via API:**
```bash
curl -X POST http://localhost:8000/api/v1/agent/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What crops grow best in Riyadh?"
  }'
```

### 2. Get Crop Recommendations

**Web Interface:**
- Navigate to http://localhost:3000
- Select "Crop Recommendations"
- Fill in:
  - Region (e.g., "Riyadh", "Al-Jouf", "Eastern Province")
  - Season (e.g., "winter", "summer")
  - Water availability (e.g., "abundant", "moderate", "scarce")
  - Budget in SAR

**Via API:**
```bash
curl -X POST http://localhost:8000/api/v1/agent/recommend-crops \
  -H "Content-Type: application/json" \
  -d '{
    "region": "Riyadh",
    "season": "winter",
    "water_availability": "moderate",
    "budget_sar": 50000
  }'
```

### 3. Analyze Livestock Opportunities

**Via API:**
```bash
curl -X POST http://localhost:8000/api/v1/agent/analyze-livestock \
  -H "Content-Type: application/json" \
  -d '{
    "region": "Al-Jouf",
    "livestock_type": "sheep",
    "investment_amount": 100000
  }'
```

### 4. Generate Research Reports

**Via API:**
```bash
curl -X POST http://localhost:8000/api/v1/agent/generate-report \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Date palm cultivation in Al-Ahsa",
    "region": "Al-Ahsa"
  }'
```

The report will include:
- Executive Summary
- Current State Analysis
- Data and Statistics with references
- Market Analysis
- Forecasts
- Recommendations
- Full citation list

### 5. Get Weather Advisory

```bash
curl -X POST http://localhost:8000/api/v1/agent/weather-advisory \
  -H "Content-Type: application/json" \
  -d '{
    "region": "Riyadh",
    "days_ahead": 7
  }'
```

### 6. Explore the Interactive API Documentation

Go to http://localhost:8000/docs

Here you can:
- See all available endpoints
- Try API calls directly in the browser
- See request/response formats
- Test different parameters

---

## 💡 Common Use Cases

### For Researchers

**Scenario:** "I need comprehensive data on olive cultivation in Saudi Arabia"

```
1. Go to http://localhost:3000/chat
2. Ask: "Generate a comprehensive research report on olive cultivation
   in Saudi Arabia, including climate requirements, suitable regions,
   economic analysis, and all academic references"
3. Receive detailed report with citations
4. Click on references to access original sources
```

### For Startups

**Scenario:** "Should I start a hydroponic farm in Jeddah?"

```
1. API call or chat: "Analyze the feasibility of hydroponic farming in Jeddah.
   Include startup costs, operating expenses, potential revenue, ROI timeline,
   and market demand analysis"
2. Get comprehensive business analysis
3. Generate financial projections
4. Access market data
```

### For Students

**Scenario:** "I need to understand Saudi agricultural challenges"

```
Chat: "Explain the main challenges facing agriculture in Saudi Arabia,
including water scarcity, climate conditions, and potential solutions.
Include statistical data and recent developments."
```

### For Investors

**Scenario:** "Where should I invest in agriculture?"

```
Chat: "Compare investment opportunities in:
1. Date palm farming in Al-Ahsa
2. Greenhouse vegetables in Tabuk
3. Sheep farming in Northern Borders

Include ROI estimates, risk analysis, and market trends for each."
```

---

## 🔍 Testing the System

### 1. Check if Services Are Running

```bash
# Check backend
curl http://localhost:8000/health

# Should return: {"status": "healthy"}
```

### 2. Test the AI Agent

```bash
curl -X POST http://localhost:8000/api/v1/agent/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is RBAT?"}'
```

Should return a JSON response with the AI's answer.

### 3. Check Database Connection

```bash
# View logs
docker-compose logs backend

# Should see: "Database connected successfully"
```

---

## 🛠️ Troubleshooting

### Problem: "Cannot connect to database"

**Solution:**
```bash
# Restart services
docker-compose down
docker-compose up

# Or check database logs
docker-compose logs postgres
```

### Problem: "Anthropic API error"

**Solution:**
1. Check your API key in `.env` file
2. Verify it's valid at https://console.anthropic.com/
3. Check you have credits available
4. Ensure no extra spaces in the key

### Problem: "Port already in use"

**Solution:**
```bash
# Find what's using the port
lsof -i :8000  # or :3000

# Kill the process or change ports in docker-compose.yml
```

### Problem: "No data returned from API"

**Solution:**
The database starts empty. You need to add data:

```bash
# Run data population script (to be created)
docker-compose exec backend python scripts/populate_sample_data.py
```

### Problem: "Frontend won't load"

**Solution:**
```bash
# Check logs
docker-compose logs frontend

# Rebuild frontend
docker-compose up --build frontend
```

---

## 📊 Adding Your Own Data

### Option 1: Via API (Recommended)

You can add data through the API endpoints:

```bash
# Add a crop
curl -X POST http://localhost:8000/api/v1/crops \
  -H "Content-Type: application/json" \
  -d '{
    "name_english": "Wheat",
    "name_arabic": "قمح",
    "category": "cereals",
    "description": "Winter cereal crop",
    "optimal_temperature": 15-25,
    "water_requirement": "moderate"
  }'
```

### Option 2: Via Database Import

```bash
# Import CSV data
docker-compose exec backend python scripts/import_data.py --file crops.csv

# Or connect directly to database
docker-compose exec postgres psql -U rbat_user -d rbat_db
```

### Option 3: Via Admin Panel (Future Feature)

Coming soon: Web-based admin interface for data management.

---

## 🎓 Learning Resources

### Understanding the Architecture

1. **Backend (Python/FastAPI):**
   - Handles all data and AI processing
   - Located in `/backend` folder
   - Entry point: `backend/app/main.py`

2. **Frontend (Next.js/React):**
   - User interface
   - Located in `/frontend` folder
   - Main pages in `frontend/src/pages/`

3. **AI Agent (Claude + RAG):**
   - Core intelligence
   - Located in `backend/app/agents/`
   - Uses RAG (Retrieval-Augmented Generation) for accuracy

4. **Database (PostgreSQL):**
   - Stores all agricultural data
   - Uses pgvector for semantic search
   - Models defined in `backend/app/models/`

### Key Files to Understand

- `backend/app/agents/agriculture_agent.py` - Main AI agent
- `backend/app/agents/rag_system.py` - Data retrieval system
- `backend/app/api/agent.py` - API endpoints
- `frontend/src/pages/chat.tsx` - Chat interface
- `docker-compose.yml` - Service configuration

---

## 🚀 Next Steps

### Immediate Actions:
1. ✅ Get platform running
2. ✅ Test the chat interface
3. ✅ Try different queries
4. ✅ Explore API documentation

### Short-term (This Week):
1. Add sample agricultural data
2. Configure external APIs (weather, news)
3. Customize AI prompts for your needs
4. Set up data collection pipelines

### Long-term (This Month):
1. Deploy to cloud (AWS/GCP/Azure)
2. Add authentication and user accounts
3. Import comprehensive Saudi agricultural data
4. Build custom reports and dashboards
5. Set up automated data updates

---

## 💬 Getting Help

### Documentation
- **API Reference:** Check `/docs/API.md`
- **Deployment Guide:** Check `/docs/DEPLOYMENT.md`
- **In-browser API Docs:** http://localhost:8000/docs

### Common Commands

```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Restart a service
docker-compose restart backend

# Rebuild after code changes
docker-compose up --build

# Access backend shell
docker-compose exec backend bash

# Access database
docker-compose exec postgres psql -U rbat_user -d rbat_db
```

---

## ✨ Tips for Best Results

1. **Be Specific:** "What crops grow in Riyadh in winter?" vs "What crops?"
2. **Include Context:** Mention region, budget, timeline
3. **Ask Follow-ups:** The chat maintains conversation history
4. **Request Citations:** Ask "with references" for academic sources
5. **Use Templates:** Check report templates for common use cases

---

## 🎯 Success Checklist

- [ ] Docker installed and running
- [ ] Repository cloned
- [ ] `.env` file configured with API keys
- [ ] Services started with `docker-compose up`
- [ ] Backend accessible at http://localhost:8000
- [ ] Frontend accessible at http://localhost:3000
- [ ] Chat interface works
- [ ] API returns responses
- [ ] Can ask questions and get answers with citations

---

**You're all set! Start asking questions and exploring Saudi agriculture data!** 🌾

For advanced features and customization, check the other documentation files in the `/docs` folder.
