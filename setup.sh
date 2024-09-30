#!/bin/bash

# Install Poetry if not already installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry could not be found, installing..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Install dependencies
poetry install

# Create logs directory if it doesn't exist
if [ ! -d "logs" ]; then
    mkdir logs
    echo "Created logs directory."
fi

# Check if .env file exists
if [ ! -f .env ]; then
    # Create .env file
    touch .env
fi

# Check if GROQ_API_KEY is already set and has a value
if grep -q "GROQ_API_KEY=" .env; then
    groq_api_key=$(grep "GROQ_API_KEY=" .env | cut -d '=' -f2)
    if [ -z "$groq_api_key" ]; then
        read -p "Please enter your GROQ API key: " groq_api_key
        sed -i "s/GROQ_API_KEY=.*/GROQ_API_KEY=$groq_api_key/" .env
    else
        echo "GROQ_API_KEY is already set in .env file."
    fi
else
    # Prompt user for API key if GROQ_API_KEY is not set
    read -p "Please enter your GROQ API key: " groq_api_key
    echo "GROQ_API_KEY=$groq_api_key" >> .env
fi

echo "Setup complete. You can now run the CLI tool."