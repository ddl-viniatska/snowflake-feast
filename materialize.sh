#!/bin/bash
set -x
echo "Starting materializing"
cd /features/snowflake-feast
CURRENT_TIME=$(date -u +"%Y-%m-%dT%H:%M:%S")
feast materialize 2022-09-15T19:20:01 $CURRENT_TIME
echo "Finished materializing"
