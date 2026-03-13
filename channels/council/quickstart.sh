#!/bin/bash
# Council of Personas - Quick Start Script

set -e

echo "🗣️  Council of Personas - Quick Start"
echo "====================================="
echo

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Install it first."
    exit 1
fi

# Check dependencies
echo "📦 Checking dependencies..."
if ! python3 -c "import google.generativeai" 2>/dev/null; then
    echo "Installing google-generativeai..."
    pip install -q google-generativeai
fi

if ! python3 -c "import rich" 2>/dev/null; then
    echo "Installing rich..."
    pip install -q rich
fi

echo "✅ Dependencies OK"
echo

# Check API key
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️  GOOGLE_API_KEY not set"
    echo
    read -p "Enter your Google AI API key: " api_key
    export GOOGLE_API_KEY="$api_key"
fi

# Launch
echo "🚀 Launching Council..."
echo
python3 council.py --chaos

