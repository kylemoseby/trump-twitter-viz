import json
from StdSuites import null

import tweepy
import tweepyAuth

username = 'nordicbuckskin'

auth = tweepy.OAuthHandler(tweepyAuth.consumer_key, tweepyAuth.consumer_secret)

auth.set_access_token(tweepyAuth.access_token, tweepyAuth.access_token_secret)

_twitter = tweepy.API(auth)

def getFavsMeta():

    user =  _twitter.get_user(username)

    return user

def printKeys(_fav):
    # Meta Info
    favKeys = _fav.__dict__.keys()

    print 'the available keys for this query are: {'

    for key in favKeys:
        print '   ' + key


def getFavs(_user):

    # Calc total number of favorites
    favCount = _user.favourites_count
    pages = favCount /20

    apiRequests = 3

    print 'there are ' + favCount.__str__() + ' favorites across ' + pages.__str__() + ' pages'

    favs = []

    # Get data from Twitter and append to favs
    ind = 1

    while ind <= apiRequests:
        print 'Getting page ' + ind.__str__() + ' of ' + pages.__str__()

        favsPage = _twitter.favorites(page=ind)

        favs.extend(favsPage)

        if 0 == ind:
            printKeys(favsPage[0])

        ind += 1

    return favs



def processFavs(favClass):

    processedFavs = []

    for favStatus in favClass:

        favorite = {
            # FIX LATER
            # have to remove attribute _api value is a Class
            # 'user' : favStatus.user.__dict__,
            # 'author' : favStatus.author.__dict__,
            'contributors': favStatus.contributors,
            'truncated': favStatus.truncated,
            'text': favStatus.text,
            'is_quote_status': favStatus.is_quote_status,
            'in_reply_to_status_id': favStatus.in_reply_to_status_id,
            'id': favStatus.id,
            'favorite_count': favStatus.favorite_count,
            # 'coordinates': favStatus.coordinates,
            'entities': favStatus.entities,
            'in_reply_to_screen_name': favStatus.in_reply_to_screen_name,
            'id_str': favStatus.id_str,
            'retweet_count': favStatus.retweet_count,
            'in_reply_to_user_id': favStatus.in_reply_to_user_id,
            'favorited': favStatus.favorited,
            'source_url': favStatus.source_url,
            # 'geo': favStatus.geo,
            'in_reply_to_user_id_str': favStatus.in_reply_to_user_id_str,
            'lang': favStatus.lang,
            # 'created_at': favStatus.created_at,
            'in_reply_to_status_id_str': favStatus.in_reply_to_status_id_str,
            # 'place': favStatus.place,
            'source': favStatus.source,
            'retweeted': favStatus.retweeted
        }

        # favorite.user._api = None

        processedFavs.append(favorite)

    return processedFavs


def createFile(favList):

    filename = 'twitter_favs_' + username + '.json'

    with open(filename, 'w') as file_object:
        json.dump(favList, file_object)


        # for item in favList:
        #     file_object.write("%s\n" % item.text.encode('utf-8'))

user = getFavsMeta()

userFavs = getFavs(user)

favsProcessed = processFavs(userFavs)

createFile(favsProcessed)
