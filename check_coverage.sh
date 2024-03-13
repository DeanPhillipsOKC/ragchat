#!/bin/bash
# Run tests with coverage
coverage run -m pytest
# Generate coverage report
coverage report -m
# Check if coverage is less than 90% and fail if so
coverage report -m | awk '/TOTAL/{ if ($NF < 90) { exit 1 } }'
