import tweepy
import csv

# Twitter API credentials
consumer_key = "<your consumer key>"
consumer_secret = "<your consumer secret>"
access_token = "<your access token>"
access_token_secret = "<your access token secret>"

# Authorization to access Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# List of airlines to collect tweets for
airlines = ["AmericanAir", "Delta", "SouthwestAir", "united", "USAirways", "VirginAmerica"]

# Open a csv file to store the tweets
with open('tweets.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["airline", "text", "created_at", "retweet_count", "favorite_count"])

    # Collect tweets for each airline
    for airline in airlines:
        tweets = tweepy.Cursor(api.search,
                               q=airline,
                               lang="en",
                               tweet_mode='extended').items(100)
        for tweet in tweets:
            writer.writerow([airline, tweet.full_text, tweet.created_at, tweet.retweet_count, tweet.favorite_count])

print("Tweets collected and saved to Tweets.csv")
