import json as js
import sys

# Initialize the output dictionary
output = {}

# Read JSON dictionary from sys.stdin
for line in sys.stdin:
    json_data = js.loads(line)

    # Get the key and value directly
    key = list(json_data.keys())[0]
    value = json_data[key]

    # Calculate the sum
    favorite_sum = sum(entry['favorite_count'] for entry in value)
    retweet_sum = sum(entry['retweet_count'] for entry in value)
    url_sum = sum(1 for entry in value if len(entry['entities']['urls']) > 0)

    output[key] = {
        'favorite_sum': int(favorite_sum),
        'retweet_sum': int(retweet_sum),
        'url_sum': int(url_sum)
    }

    # Calculate mean and pct
    count = len(value)+1
    output[key]['favorite_mean'] = output[key]['favorite_sum'] / count
    output[key]['retweet_mean'] = output[key]['retweet_sum'] / count
    output[key]['url_pct'] = output[key]['url_sum'] / count

# Print the output dictionary
for key, values in output.items():
    print(f"{key}\t{values}")
