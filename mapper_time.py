#!/usr/bin/env python3

import json as js
import sys
import time
import argparse

# Function to parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--delay', type=float, default=0, help='Time delay for experiment')
    return parser.parse_args()

# Read command-line arguments
args = parse_args()
delay = args.delay

# Read JSON dictionary from sys.stdin
for line in sys.stdin:

    # Time delay for experiment
    time.sleep(delay)

    json_data = js.loads(line)

    # Get the key and value directly
    key = list(json_data.keys())[0]
    value = json_data[key]

    # Loop through every value
    for entry in value:

        # Calculate the sum
        favorite = entry['favorite_count']
        retweet = entry['retweet_count']
        url = 1 if len(entry['entities']['urls']) > 0 else 0

        # Output
        print("%s\t%s\t%s\t%s" % (key, favorite, retweet, url))
