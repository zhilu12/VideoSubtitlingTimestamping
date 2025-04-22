#!/bin/bash

# Check python and pip
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed"
    exist 1
fi

if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed"
    exit 1
fi

# Intsalling Python Dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt




# Check and install ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "ffmpeg not found. Attempting to install..."

    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update
        sudo apt install -y ffmpeg
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew &> /dev/null; then
            echo "Homebrew not found. Please install Homebrew to proceed."
            exit 1
        fi
        brew install ffmpeg
    else
        echo "Unrecognized OS. Please install ffmpeg manually: https://ffmpeg.org/download.html"
    fi
else
    echo "ffmpeg already installed."
fi

echo "Setup complete!"
