
import tweepy

consumer_key = "UjvnnI5xmlXtVvEul0TAJLfhW"
consumer_secret = "GhL64awHhY0AFDsvgnDqk4GKi4effujoF9wer5BVSMZWtMvn8o"
access_token = "10016002-QfV3j6RSev1gBurSNu4d7rU4CbwfQOn4IRzpLSUzV"
access_token_secret = "vK3Gq9kSDaOTQMYux3JzV752I0xJ1FR6sgrGMNUHUEGV6"

username = 'nordicbuckskin'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
_twitter = tweepy.API(auth)
