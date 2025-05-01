#!/bin/bash
set -e

# Install build dependencies
python -m pip install --upgrade pip
pip install wheel setuptools
pip install build

# Install Pillow with specific build flags
LDFLAGS="-L/opt/homebrew/lib" CFLAGS="-I/opt/homebrew/include" pip install Pillow==9.5.0

# Install remaining dependencies
pip install -r requirements.txt

# Set Django settings
export DJANGO_SETTINGS_MODULE=tradingbot.settings

# Run Django commands
python manage.py collectstatic --noinput
python manage.py migrate