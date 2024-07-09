#!/bin/bash

# turn on bash's job control
set -m

alembic upgrade head

# Start the primary process and put it in the background
echo "Starting server"
python -m src

## Start the migrate process
#echo "Apply database migrations"

# now we bring the primary process back into the foreground
# and leave it there
fg %1