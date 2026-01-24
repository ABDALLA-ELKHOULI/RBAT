#!/bin/bash

echo "🌾 Starting RBAT Frontend"
echo "========================="
echo ""

# Navigate to frontend
cd frontend

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing Node.js dependencies (this may take a few minutes)..."
    npm install
fi

echo ""
echo "🚀 Starting Frontend..."
echo "   Frontend will run on: http://localhost:3000"
echo "   Chat interface: http://localhost:3000/chat"
echo ""
echo "   Press Ctrl+C to stop"
echo ""

# Start frontend
npm run dev
