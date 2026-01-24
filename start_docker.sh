#!/bin/bash

echo "🐳 Starting RBAT with Docker"
echo "============================"
echo ""

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "❌ Docker command not found!"
    echo ""
    echo "Please make sure Docker is installed and running:"
    echo ""
    echo "For Windows/Mac:"
    echo "  1. Open Docker Desktop application"
    echo "  2. Wait until it's running (green indicator)"
    echo "  3. Then run this script again"
    echo ""
    echo "For Linux:"
    echo "  sudo service docker start"
    echo "  # OR"
    echo "  sudo systemctl start docker"
    echo ""
    exit 1
fi

# Check if Docker daemon is running
if ! docker ps &> /dev/null; then
    echo "❌ Docker is installed but not running!"
    echo ""
    echo "Please start Docker:"
    echo ""
    echo "For Windows/Mac:"
    echo "  Open Docker Desktop application"
    echo ""
    echo "For Linux:"
    echo "  sudo service docker start"
    echo ""
    exit 1
fi

echo "✅ Docker is running!"
echo ""

# Check for API key in .env
if [ ! -f ".env" ]; then
    echo "⚠️  Creating .env file from template..."
    cp .env.example .env
    echo "❌ Please add your Anthropic API key to .env file"
    echo ""
    echo "Edit .env and change:"
    echo "  ANTHROPIC_API_KEY=your_anthropic_api_key_here"
    echo "To:"
    echo "  ANTHROPIC_API_KEY=sk-ant-your-real-key"
    echo ""
    exit 1
fi

if grep -q "ANTHROPIC_API_KEY=your_anthropic_api_key_here" .env; then
    echo "❌ Please add your Anthropic API key to .env file"
    echo ""
    echo "Get your key from: https://console.anthropic.com/"
    echo ""
    echo "Edit .env and change:"
    echo "  ANTHROPIC_API_KEY=your_anthropic_api_key_here"
    echo "To:"
    echo "  ANTHROPIC_API_KEY=sk-ant-your-real-key"
    echo ""
    exit 1
fi

echo "✅ API key is configured"
echo ""

# Check docker-compose or docker compose
if docker compose version &> /dev/null; then
    COMPOSE_CMD="docker compose"
elif command -v docker-compose &> /dev/null; then
    COMPOSE_CMD="docker-compose"
else
    echo "❌ Docker Compose not found!"
    echo "Please install Docker Compose"
    exit 1
fi

echo "🚀 Starting RBAT services..."
echo ""
echo "This will start:"
echo "  - PostgreSQL database with pgvector"
echo "  - Redis cache"
echo "  - Backend API (Python/FastAPI)"
echo "  - Frontend (Next.js)"
echo ""
echo "First time will take 5-10 minutes to download images..."
echo ""

# Start services
$COMPOSE_CMD up

# If user stops with Ctrl+C, clean message
echo ""
echo "Stopped. To start again, run: ./start_docker.sh"
echo "To stop and remove containers: docker compose down"
