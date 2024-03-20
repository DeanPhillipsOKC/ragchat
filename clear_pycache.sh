#!/bin/bash

# Remove __pycache__ directories and .pyc files
find . -type d -name "__pycache__" -exec rm -rf {} + || true
find . -type f -name "*.pyc" -exec rm -f {} + || true
