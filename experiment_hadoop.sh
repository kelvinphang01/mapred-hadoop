#!/bin/bash

# Define the delay values
delays=(0 0.01 0.02 0.03 0.04)

# Run the script for each delay value
for delay in "${delays[@]}"; do

    # Measure the execution time using the time command
    time mapred streaming \
        -files mapper_time.py,reducer.py \
        -input fakenewsnet/timeline.json \
        -output fnn_delay_"$delay" \
        -mapper "python3 mapper_time.py --delay $delay" \
        -reducer "python3 reducer.py"
    echo "Job executed with delay = $delay"
done
