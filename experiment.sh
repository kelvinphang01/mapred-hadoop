#!/bin/bash

# Define the delay values
delays=(0 0.01 0.02 0.03 0.04)

# Run the script for each delay value
for delay in "${delays[@]}"; do
    echo "Running with delay = $delay"
    # Measure the execution time using the time command
    time cat timeline.json | python3 mapper_time.py --delay "$delay" | python3 reducer.py > "results_${delay}.txt"
done
