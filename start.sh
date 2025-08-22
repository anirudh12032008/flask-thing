#!/bin/bash
echo "Starting Flask app on port 42633..."

PORT=42633

# Update code from GitHub
echo "Pulling latest code..."
if ! git pull; then
  echo "git pull failed"
  exit 1
fi

# Set up virtual environment
echo "Setting up virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Start Flask app with Gunicorn
echo "Starting Flask app..."
exec gunicorn -b "0.0.0.0:$PORT" main:app
