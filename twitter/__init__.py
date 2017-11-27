# import tweepyAuth
#
# consumer_key = "UjvnnI5xmlXtVvEul0TAJLfhW"
# consumer_secret = "GhL64awHhY0AFDsvgnDqk4GKi4effujoF9wer5BVSMZWtMvn8o"
# access_token = "10016002-QfV3j6RSev1gBurSNu4d7rU4CbwfQOn4IRzpLSUzV"
# access_token_secret = "vK3Gq9kSDaOTQMYux3JzV752I0xJ1FR6sgrGMNUHUEGV6"
#
# auth = tweepyAuth.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# api = tweepyAuth.API(auth)
#
# def checkAPIStatus():
#     status = api.rate_limit_status(api.verify_credentials())
#     print 'status'
#     print status

# def getFollowerInfo():

    # followerIDs = api.followers_ids('nordicbuckskin')

    # print followerIDs

    # checkAPIStatus()

    # for id in followerIDs:
        # print id

        # followerFollows = api.followers_ids(id)

        # checkAPIStatus()

        # for _user in followerFollows:
            # print _user


# getFollowerInfo()


# for firstgen in followfollow:
#     print firstgen
#
# follower = api.followers('nordicbuckskin')

# public_tweets = api.user_timeline('nordicbuckskin')
#
# for tweet in public_tweets:
#     print tweet.text
