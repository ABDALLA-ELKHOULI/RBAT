#!/bin/bash

# RBAT System Check Script
# This script checks if your system has all the required components

echo "🔍 RBAT System Requirements Check"
echo "=================================="
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Docker
echo "📦 Checking Docker..."
if command_exists docker; then
    echo "✅ Docker is installed: $(docker --version)"

    # Check if Docker is running
    if docker ps >/dev/null 2>&1; then
        echo "✅ Docker is running"
    else
        echo "⚠️  Docker is installed but not running"
        echo "   Start it with: sudo systemctl start docker"
    fi
else
    echo "❌ Docker is NOT installed"
    echo "   See INSTALL_DOCKER.md for installation instructions"
fi

echo ""

# Check Docker Compose
echo "🐙 Checking Docker Compose..."
if command_exists docker && docker compose version >/dev/null 2>&1; then
    echo "✅ Docker Compose is installed: $(docker compose version)"
elif command_exists docker-compose; then
    echo "✅ Docker Compose is installed: $(docker-compose --version)"
else
    echo "❌ Docker Compose is NOT installed"
    echo "   Install with Docker or see INSTALL_DOCKER.md"
fi

echo ""

# Check Python
echo "🐍 Checking Python..."
if command_exists python3; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo "✅ Python is installed: $PYTHON_VERSION"

    # Check if version is 3.11+
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

    if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 11 ]; then
        echo "✅ Python version is compatible (need 3.11+)"
    else
        echo "⚠️  Python version is $PYTHON_VERSION (need 3.11+)"
    fi
else
    echo "❌ Python is NOT installed"
    echo "   Install with: sudo apt-get install python3.11"
fi

echo ""

# Check Node.js
echo "📗 Checking Node.js..."
if command_exists node; then
    NODE_VERSION=$(node --version 2>&1)
    echo "✅ Node.js is installed: $NODE_VERSION"

    # Check if version is 18+
    NODE_MAJOR=$(echo $NODE_VERSION | cut -d. -f1 | sed 's/v//')

    if [ "$NODE_MAJOR" -ge 18 ]; then
        echo "✅ Node.js version is compatible (need 18+)"
    else
        echo "⚠️  Node.js version is $NODE_VERSION (need 18+)"
    fi
else
    echo "❌ Node.js is NOT installed"
    echo "   Install with: curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -"
    echo "                 sudo apt-get install -y nodejs"
fi

echo ""

# Check PostgreSQL
echo "🐘 Checking PostgreSQL..."
if command_exists psql; then
    PSQL_VERSION=$(psql --version 2>&1)
    echo "✅ PostgreSQL client is installed: $PSQL_VERSION"
else
    echo "❌ PostgreSQL is NOT installed"
    echo "   Install with: sudo apt-get install postgresql postgresql-contrib"
fi

echo ""

# Check Redis
echo "📮 Checking Redis..."
if command_exists redis-cli; then
    REDIS_VERSION=$(redis-cli --version 2>&1)
    echo "✅ Redis is installed: $REDIS_VERSION"
else
    echo "⚠️  Redis is NOT installed (optional but recommended)"
    echo "   Install with: sudo apt-get install redis-server"
fi

echo ""

# Check .env file
echo "🔐 Checking .env configuration..."
if [ -f ".env" ]; then
    echo "✅ .env file exists"

    # Check for API key
    if grep -q "ANTHROPIC_API_KEY=sk-ant-" .env; then
        echo "✅ Anthropic API key appears to be configured"
    elif grep -q "ANTHROPIC_API_KEY=your_anthropic_api_key_here" .env; then
        echo "❌ Anthropic API key is using placeholder value"
        echo "   Get your key from https://console.anthropic.com/"
        echo "   Edit .env and replace: ANTHROPIC_API_KEY=sk-ant-your-real-key"
    else
        echo "⚠️  Anthropic API key may not be configured correctly"
    fi
else
    echo "❌ .env file does NOT exist"
    echo "   Create it with: cp .env.example .env"
    echo "   Then edit it and add your ANTHROPIC_API_KEY"
fi

echo ""
echo "=================================="
echo "📋 Summary & Recommendations"
echo "=================================="
echo ""

# Determine recommended path
if command_exists docker && docker ps >/dev/null 2>&1; then
    echo "✅ RECOMMENDED: Use Docker (easiest method)"
    echo ""
    echo "   Quick start:"
    echo "   1. Make sure .env file has your ANTHROPIC_API_KEY"
    echo "   2. Run: docker compose up"
    echo "   3. Open: http://localhost:3000/chat"
    echo ""
    echo "   See GETTING_STARTED.md for details"

elif command_exists python3 && command_exists node; then
    echo "✅ RECOMMENDED: Manual Setup (without Docker)"
    echo ""
    echo "   You have Python and Node.js but Docker is not available."
    echo "   Follow the manual setup guide:"
    echo ""
    echo "   See MANUAL_SETUP.md for step-by-step instructions"

else
    echo "⚠️  REQUIRED: Install Prerequisites"
    echo ""
    echo "   You need to install required software first."
    echo ""
    echo "   Option 1 (Easiest): Install Docker"
    echo "   - See INSTALL_DOCKER.md"
    echo ""
    echo "   Option 2: Install Python + Node.js + PostgreSQL"
    echo "   - See MANUAL_SETUP.md"
fi

echo ""
