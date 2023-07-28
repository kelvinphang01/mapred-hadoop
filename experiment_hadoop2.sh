#!/bin/bash

# Define the delay values
delay=0.5

# Measure the execution time using the time command
time mapred streaming \
    -files mapper_time.py,reducer.py \
    -input fakenewsnet/timeline.json \
    -output fnn_delay_"$delay" \
    -mapper "python3 mapper_time.py --delay $delay" \
    -reducer "python3 reducer.py"
echo "Job executed with delay = $delay"
done
