def getStatuses(self):
    _tweets = []
    pageInd = 1

    print 'Getting tweets from twitter'

    while _tweets.__len__() < 3:
        # while _tweets.__len__() < self.user.statuses_count:

        # print 'Getting page ' + ' //  ' + ' of ' + self.user.statuses_count
        print pageInd.__str__()
        print _tweets.__len__()

        _tweets.extend(_twitter_.user_timeline(count='1'))

        pageInd += 1

    # KEYS
    print 'status obj keys for this query are:'

    statusKeys = _tweets[0].__dict__.keys()

    for key in statusKeys:
        print ':   ' + key

    print _tweets

    self.tweets = _tweets

    return _tweets


# import json
# import tweepy
# import tweepyAuth
#
# username = 'nordicbuckskin'
#
# auth = tweepy.OAuthHandler(tweepyAuth.consumer_key, tweepyAuth.consumer_secret)
#
# auth.set_access_token(tweepyAuth.access_token, tweepyAuth.access_token_secret)
#
# _twitter = tweepy.API(auth)
#
#
# apiRequests = 3
#
#
# def getStatuses(_user):
#
#     statuses = _twitter.user_timeline(count='10')
#
#     # KEYS
#     # print 'the available keys for this query are:'
#     #
#     # statusKeys =  statuses[0].__dict__.keys()
#     #
#     # for key in statusKeys:
#     #     print ':   ' + key
#
#     # print statuses
#
#
#     return statuses
# def processStatuses(statusClassList):
#
#     processedList = []
#
#     def userClassJSON(userClass):
#         print userClass
#         return {}
#
#     for _class_ in statusClassList:
#
#         # print _class_
#
#         processedList.append({
#             # 'user' : userClassJSON(_class_.user),
#             'contributors' : _class_.contributors,
#             'truncated' : _class_.truncated,
#             'text' : _class_.text,
#             'is_quote_status' : _class_.is_quote_status,
#             'in_reply_to_status_id' : _class_.in_reply_to_status_id,
#             'id' : _class_.id,
#             'favorite_count' : _class_.favorite_count,
#             # '_api' : _class_._api,
#             # 'author' : _class_.author,
#             '_json' : _class_._json,
#             'coordinates' : _class_.coordinates,
#             'entities' : _class_.entities,
#             'in_reply_to_screen_name' : _class_.in_reply_to_screen_name,
#             'id_str' : _class_.id_str,
#             'retweet_' : _class_.retweet_count,
#             'in_reply_to_user_id' : _class_.in_reply_to_user_id,
#             'favorited' : _class_.favorited,
#             # 'retweeted_status' : _class_.retweeted_status,
#             'source_url' : _class_.source_url,
#             # 'geo' : _class_.geo,
#             'in_reply_to_user_id_str' : _class_.in_reply_to_user_id_str,
#             'lang' : _class_.lang,
#             # 'created_at' : _class_.created_at,
#             'in_reply_to_status_id_str' : _class_.in_reply_to_status_id_str,
#             # 'place' : _class_.place,
#             'source' : _class_.source,
#             'retweeted' : _class_.retweeted,
#         })
#
#     return processedList
#
# def createFile(statusList):
#
#     filename = 'twitter_statuses_' + username + '.json'
#
#     with open(filename, 'w') as file_object:
#         json.dump(statusList, file_object)
#
#
# userStatuses = getStatuses(username)
#
# statusProcessed = processStatuses(userStatuses)
#
# for key in statusProcessed[0].keys():
#     print key
#
# createFile(statusProcessed)
