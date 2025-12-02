#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Convert static assets
python3 manage.py collectstatic --no-input

# Apply any outstanding database migrations
python3 manage.py migrate