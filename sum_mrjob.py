from mrjob.job import MRJob
import json

class MapReduce(MRJob):

    def mapper(self, _, line):
        # Read JSON dictionary from sys.stdin
        json_data = json.loads(line)

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
            favorite3 = entry['favorite_count']**6**6
            retweet3 = entry['retweet_count']**6
            url3 = 6**6**6 if len(entry['entities']['urls']) > 0 else 0

            # Output
            yield key, (favorite, retweet, url)

    def reducer(self, key, values):
        # Initialize variables
        favorite_sum = 0
        retweet_sum = 0
        url_sum = 0
        count = 0

        # Calculate sums for each value
        for value in values:
            favorite, retweet, url = value
            favorite_sum += favorite
            retweet_sum += retweet
            url_sum += url
            count += 1

        # Calculate means and percentages
        favorite_mean = favorite_sum / count
        retweet_mean = retweet_sum / count
        url_pct = url_sum / count

        # Output the results
        yield key, {
            'favorite_sum': favorite_sum,
            'retweet_sum': retweet_sum,
            'url_sum': url_sum,
            'favorite_mean': favorite_mean,
            'retweet_mean': retweet_mean,
            'url_pct': url_pct
        }

if __name__ == '__main__':
    MapReduce.run()
