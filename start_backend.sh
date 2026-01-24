#!/bin/bash

echo "🌾 Starting RBAT - Research-Based Agriculture Technology"
echo "========================================================"
echo ""

# Check if .env has API key
if grep -q "ANTHROPIC_API_KEY=your_anthropic_api_key_here" .env; then
    echo "⚠️  WARNING: You need to add your Anthropic API key to .env file"
    echo "   Edit .env and replace: ANTHROPIC_API_KEY=your_anthropic_api_key_here"
    echo "   With: ANTHROPIC_API_KEY=sk-ant-your-real-key"
    echo ""
    read -p "Press Enter after you've added your API key, or Ctrl+C to exit..."
fi

# Check PostgreSQL
echo "📊 Checking PostgreSQL..."
if pg_isready -h localhost > /dev/null 2>&1; then
    echo "✅ PostgreSQL is running"
else
    echo "❌ PostgreSQL is not running"
    echo "   Please start it with: service postgresql start"
    echo "   Or: sudo systemctl start postgresql"
    exit 1
fi

# Check Redis
echo "📮 Checking Redis..."
if redis-cli ping > /dev/null 2>&1; then
    echo "✅ Redis is running"
else
    echo "⚠️  Redis is not running (optional but recommended)"
    echo "   Start it with: redis-server --daemonize yes"
fi

echo ""
echo "🔧 Setting up backend..."

# Navigate to backend
cd backend

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install --quiet -q -r requirements.txt

echo ""
echo "🚀 Starting Backend API..."
echo "   Backend will run on: http://localhost:8000"
echo "   API Docs will be at: http://localhost:8000/docs"
echo ""
echo "   Press Ctrl+C to stop"
echo ""

# Start backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
