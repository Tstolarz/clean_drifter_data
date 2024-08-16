#!/bin/bash

# Get the directory of the dragged file
FILE="$1"
DIR=$(dirname "$FILE")

# Run the Python script with the dragged file
/path/to/python3 /path/to/clean_drifter_data_app_local.py "$FILE"
