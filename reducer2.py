#!/usr/bin/env python3

import sys

# Initialize variables
current_key = None
favorite_sum = 0
retweet_sum = 0
url_sum = 0

# Read key-value pairs from standard input
for line in sys.stdin:
    # Parse the input
    key, favorite, retweet, url = line.strip().split('\t')

    # Check if the key has changed
    if current_key != key:
        # Output the result for the previous key
        if current_key:
            print("%s\t%d\t%d\t%d" % (current_key, favorite_sum, retweet_sum, url_sum))

        # Reset the variables for the new key
        current_key = key
        favorite_sum = 0
        retweet_sum = 0
        url_sum = 0

    # Accumulate the values for the current key
    favorite_sum += int(favorite)
    retweet_sum += int(retweet)
    url_sum += int(url)

# Output the result for the last key
if current_key:
    print("%s\t%d\t%d\t%d" % (current_key, favorite_sum, retweet_sum, url_sum))

