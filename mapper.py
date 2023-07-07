#!/usr/bin/env python3

import json as js
import sys

# Read JSON dictionary from sys.stdin
for line in sys.stdin:
    json_data = js.loads(line)

    # Get the key and value
    key = list(json_data.keys())[0]
    value = json_data[key]

    # Loop through every value
    for entry in value:

        # Get the 3 variables
        favorite = entry['favorite_count']
        retweet = entry['retweet_count']
        url = 1 if len(entry['entities']['urls']) > 0 else 0

        # Just to increase computational complexity
        favorite2 = entry['favorite_count']**6**6
        retweet2 = entry['retweet_count']**6
        url2 = 6**6**6 if len(entry['entities']['urls']) > 0 else 0

        # Output
        print("%s\t%s\t%s\t%s" % (key, favorite, retweet, url))
