#!/usr/bin/env python3

import sys

# Initialize the mapper_output dictionary
mapper_output = {}
current_key = None

# Read key-value pairs from sys.stdin
for line in sys.stdin:
    # Split the line into key and values
    key, favorite, retweet, url = line.strip().split('\t')

    # Check for same key
    if current_key == key:

        # If the key is same, update the sums for each value
        mapper_output[key]['favorite_sum'] += int(favorite)
        mapper_output[key]['retweet_sum'] += int(retweet)
        mapper_output[key]['url_sum'] += int(url)
        count += 1
    else:
        # Calculate mean and pct for the key
        if current_key:
            mapper_output[current_key]['favorite_mean'] = mapper_output[current_key]['favorite_sum'] / count
            mapper_output[current_key]['retweet_mean'] = mapper_output[current_key]['retweet_sum'] / count
            mapper_output[current_key]['url_pct'] = mapper_output[current_key]['url_sum'] / count

        # If the key is different, create a new entry in the mapper_output dictionary
        mapper_output[key] = {
            'favorite_sum': int(favorite),
            'retweet_sum': int(retweet),
            'url_sum': int(url)
        }
        current_key = key
        count = 1

# Process for last key
mapper_output[current_key]['favorite_mean'] = mapper_output[current_key]['favorite_sum'] / count
mapper_output[current_key]['retweet_mean'] = mapper_output[current_key]['retweet_sum'] / count
mapper_output[current_key]['url_pct'] = mapper_output[current_key]['url_sum'] / count

# Print the mapper_output dictionary
for key, values in mapper_output.items():
    print(f"{key}\t{values}")
