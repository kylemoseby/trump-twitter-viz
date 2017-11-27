import json
import re
import tweepy
import tweepyAuth

auth = tweepy.OAuthHandler(tweepyAuth.consumer_key, tweepyAuth.consumer_secret)

auth.set_access_token(tweepyAuth.access_token, tweepyAuth.access_token_secret)

_twitter_ = tweepy.API(auth)


class TwitterData():
  """A wrapper for getting stuff from Tweepy"""

  timelines = []
  # Queue of users to get account info for
  trump_users = []
  twitterUser = {}
  trump_data = {}

  def __init__(self):

    print 'Init for another TwitterData class'

  # DATA CALLS
  def getTwitterUser(self, username):

    self.username = username

    self.user = _twitter_.get_user(username)

    print 'Getting data for ' + self.user.name + ' @' + self.username

  def getUserTimeline(self, username):

    tweets = []

    user = _twitter_.get_user(username)

    tweet_cnt = user.statuses_count
    per_page = 200
    pages = tweet_cnt / per_page

    ind = 1

    # while ind <= pages:
    while ind <= 1:
      print 'Getting page ' + ind.__str__() + ' of ' + pages.__str__()

      page = _twitter_.user_timeline(username, count=per_page, page=ind)

      for status in page:
        tweets.append({
          'contributors': status.contributors,
          'truncated': status.truncated,
          'text': status.text,
          'is_quote_status': status.is_quote_status,
          'in_reply_to_status_id': status.in_reply_to_status_id,
          'id': status.id,
          'favorite_count': status.favorite_count,
          # '_api': status._api,
          'source': status.source,
          # 'quoted_status_id': status.quoted_status_id,
          '_json': status._json,
          'coordinates': status.coordinates,
          # 'quoted_status': status.quoted_status,
          'entities': status.entities,
          'in_reply_to_screen_name': status.in_reply_to_screen_name,
          'id_str': status.id_str,
          'retweet_count': status.retweet_count,
          'in_reply_to_user_id': status.in_reply_to_user_id,
          'favorited': status.favorited,
          'source_url': status.source_url,
          # 'user': status.user,
          # 'geo': status.geo,
          'in_reply_to_user_id_str': status.in_reply_to_user_id_str,
          # 'possibly_sensitive': status.possibly_sensitive,
          'lang': status.lang,
          # 'created_at': status.created_at,
          # 'author': status.author,
          # 'quoted_status_id_str': status.quoted_status_id_str,
          'in_reply_to_status_id_str': status.in_reply_to_status_id_str,
          # 'place': status.place,
          'retweeted': status.retweeted
        })

      ind += 1

    self.twitterUser[username] = {
      'username': username,
      'data': tweets
    }

  def getTrumpUsers(self):
    """Searches returned tweets for all the usernames being monitored by the bot TrumpAlers"""

    print "Processing Trump data..."
    print "Searching for Trump twitter username associated with this account"

    users = []

    # list of trumpsAlert tweets
    trump_tweets = self.twitterUser['trumpsAlert'].get('data');

    usrReg = re.compile("\A\S+")

    # loop through trumpAlerts tweets
    for tweet in trump_tweets:

      # Probably a better way to do this
      tweet_text = tweet['text']

      # usrname = usrReg.search(tweet_text)

      test = re.match(usrReg, tweet_text)
      t2 = test.group(0)

      # Check if username is already in userlist
      if t2 not in users:
        users.append(t2)

    # Need to decided if one class will be for one twitter user
    self.trump_users = users

    print 'The following usernames were found:'
    for usr in users:
      print '   ' + usr

  def getTrumpUserData(self):
    print "Getting Twitter user data..."

    for username in self.trump_users:
      print ":      " + username
      self.trump_data[username] = _twitter_.get_user(username)
      print "...  done"

    print "All data from Twitter has been got."

  def createFile(self):

    print 'saving JSON file to disk'

    # write username.json file
    userJSON = 'app/data/twitter_user_' + self.username + '.json'
    with open(userJSON, 'w') as file_object:
      json.dump(self.user._json, file_object)

      print userJSON + ' written to disk'

    # write trump users file
    # Process trumpusers for JSON
    json_trump = {}

    for key, usr in self.trump_data.iteritems():
      _user_ = usr.__dict__

      json_trump[key] = _user_['_json']

    trumpUsers = 'app/data/twitter_userinfo_trumps.json'
    print "Writing " + trumpUsers + " to the disk"
    with open(trumpUsers, 'w') as file_object:
      json.dump(json_trump, file_object)

      print trumpUsers + ' written to disk'


    # Prep statuses for JSON
    for timeline in self.twitterUser:

      print "Writing timelines to disk"

      timeline_data = self.twitterUser[timeline]

      # write status.json file
      tweetsJSON = 'app/data/twitter_statuses_' + timeline + '.json'
      with open(tweetsJSON, 'w') as file_object:
        json.dump(timeline_data, file_object)

        print tweetsJSON + ' written to disk'

        # Old code to load users in a List for Angular   Keeping for records
        # jsonTrumps = []
        # for key, usr in self.trumpData.iteritems():
        #     jsonTrumps.append(usr._json)
