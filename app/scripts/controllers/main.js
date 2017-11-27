'use strict';

var twttr = twttr || {};

/**
 * @ngdoc function
 * @name sandboxApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the sandboxApp
 */
angular.module('sandboxApp')
  .controller('MainCtrl', [function() {}])
  .controller('twitterCtrl', ['$scope', '$http', function($scope, $http) {

    var localserve = 'http://localhost:8080/';

    // GET DATA
    var dataOpts = [{
      id: 'trumpUsers',
      url: 'trumpFamily'
      // url: 'twitter_userinfo_trumps.json',
    }, {
      id: 'statuses',
      url: 'trumpsAlertTimeline'
      // url: 'twitter_statuses_trumpsAlert.json',
    }, {
      id: 'user',
      url: 'trumpsAlertuserObj'
      // url: 'twitter_user_trumpsAlert.json',
    }];

    function getTwitterData(opts) {
      $http({
        method: 'GET',
        url: localserve + opts.url
      }).then(function successCallback(response) {

        $scope[opts.id] = response.data;

      }, function errorCallback(response) {

        $scope.error = response;

        console.log(response);
      });
    }

    for (var i = dataOpts.length - 1; i >= 0; i--) {
      getTwitterData(dataOpts[i]);
    }
    // END DATA CALLS

    // VIEW OPTS
    $scope._opts = {
      ind: 15,
      step: 5
    };

  }])
  .directive('trumpTweet', [function() {
    // Runs during compile
    return {
      templateUrl: 'trump_views/trump_tweet.html',
      link: function($scope) {
        // Rewrite as regular exp
        $scope.trmpuser = $scope.tweet.text.slice(0, $scope.tweet.text.indexOf(' '));

        $scope.twitterDate = function(_tweetDate){
          return new Date(_tweetDate);
        };

        $scope.trumpUserImg = function(_usr){
          return $scope.$parent.trumpUsers[_usr].profile_image_url_https;
        };

      }
    };
  }]);

/*
  status = {
    "contributors": null,
    "truncated": false,
    "text": "RT @DPRK_News: Shift from \"daylight saving\" to standard time in west is government project to liquidate excess population through accidents…",
    "is_quote_status": false,
    "in_reply_to_status_id": null,
    "id": 927067558271791100,
    "favorite_count": 0,
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "retweeted": true,
    "coordinates": null,
    "entities": { "symbols": [],
    "user_mentions": [{ "id": 58569513,
    "indices": [3, 13],
    "id_str": "58569513",
    "screen_name": "DPRK_News",
    "name": "DPRK News Service [OFFICIAL AND AUTHORIZED]" }],
    "hashtags": [],
    "urls": [] },
    "in_reply_to_screen_name": null,
    "in_reply_to_user_id": null,
    "retweet_count": 749,
    "id_str": "927067558271791111",
    "favorited": false,
    "retweeted_status": { "contributors": null,
    "truncated": false,
    "text": "Shift from \"daylight saving\" to standard time in west is government project to liquidate excess population through accidents and depression.",
    "is_quote_status": false,
    "in_reply_to_status_id": null,
    "id": 925745061303857200,
    "favorite_count": 1431,
    "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
    "retweeted": true,
    "coordinates": null,
    "entities": { "symbols": [],
    "user_mentions": [],
    "hashtags": [],
    "urls": [] },
    "in_reply_to_screen_name": null,
    "in_reply_to_user_id": null,
    "retweet_count": 749,
    "id_str": "925745061303857152",
    "favorited": false,
    "user": { "follow_request_sent": false,
    "has_extended_profile": false,
    "profile_use_background_image": true,
    "default_profile_image": false,
    "id": 58569513,
    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/24404264/north_korea_jan_2003.jpg",
    "verified": false,
    "translator_type": "none",
    "profile_text_color": "333333",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/323235980/dprk-flag_normal.gif",
    "profile_sidebar_fill_color": "DDFFCC",
    "entities": { "url": { "urls": [{ "url": "https://t.co/Dkq1nJO2sa",
    "indices": [0, 23],
    "expanded_url": "http://www.mfa.gov.kp/en/",
    "display_url": "mfa.gov.kp/en/" }] },
    "description": { "urls": [] } },
    "followers_count": 280728,
    "profile_sidebar_border_color": "BDDCAD",
    "id_str": "58569513",
    "profile_background_color": "9AE4E8",
    "listed_count": 2447,
    "is_translation_enabled": false,
    "utc_offset": 32400,
    "statuses_count": 5734,
    "description": "Official News feed of Democratic Peoples Republic of Korea",
    "friends_count": 100,
    "location": "Pyongyang, DPRK",
    "profile_link_color": "267491",
    "profile_image_url": "http://pbs.twimg.com/profile_images/323235980/dprk-flag_normal.gif",
    "following": true,
    "geo_enabled": false,
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/58569513/1489847019",
    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/24404264/north_korea_jan_2003.jpg",
    "screen_name": "DPRK_News",
    "lang": "en",
    "profile_background_tile": true,
    "favourites_count": 0,
    "name": "DPRK News Service",
    "notifications": false,
    "url": "https://t.co/Dkq1nJO2sa",
    "created_at": "Mon Jul 20 19:45:37 +0000 2009",
    "contributors_enabled": false,
    "time_zone": "Seoul",
    "protected": false,
    "default_profile": false,
    "is_translator": false },
    "geo": null,
    "in_reply_to_user_id_str": null,
    "lang": "en",
    "created_at": "Wed Nov 01 15:23:16 +0000 2017",
    "in_reply_to_status_id_str": null,
    "place": null },
    "user": { "follow_request_sent": false,
    "has_extended_profile": false,
    "profile_use_background_image": false,
    "default_profile_image": false,
    "id": 10016002,
    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/324708655/black_flag_background.png",
    "verified": false,
    "translator_type": "none",
    "profile_text_color": "000000",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/918696559386148864/npPzpGrh_normal.jpg",
    "profile_sidebar_fill_color": "FAFAFA",
    "entities": { "description": { "urls": [] } },
    "followers_count": 232,
    "profile_sidebar_border_color": "000000",
    "id_str": "10016002",
    "profile_background_color": "FFFFFF",
    "listed_count": 6,
    "is_translation_enabled": false,
    "utc_offset": -28800,
    "statuses_count": 3176,
    "description": "🆓",
    "friends_count": 518,
    "location": "",
    "profile_link_color": "585830",
    "profile_image_url": "http://pbs.twimg.com/profile_images/918696559386148864/npPzpGrh_normal.jpg",
    "following": false,
    "geo_enabled": false,
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/10016002/1507909926",
    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/324708655/black_flag_background.png",
    "screen_name": "nordicbuckskin",
    "lang": "en",
    "profile_background_tile": true,
    "favourites_count": 1825,
    "name": "💤💤💤💤",
    "notifications": false,
    "url": null,
    "created_at": "Wed Nov 07 00:30:42 +0000 2007",
    "contributors_enabled": false,
    "time_zone": "Pacific Time (US & Canada)",
    "protected": false,
    "default_profile": false,
    "is_translator": false },
    "geo": null,
    "in_reply_to_user_id_str": null,
    "lang": "en",
    "created_at": "Sun Nov 05 06:58:24 +0000 2017",
    "in_reply_to_status_id_str": null,
    "place": null
  }

  user = {
    contributors_enabled : false
    created_at : "Mon Jan 23 04:14:28 +0000 2012"
    default_profile : false
    default_profile_image : false
    description : "Counselor to the President"
    entities : {description: {…}}
    favourites_count : 2318
    follow_request_sent : false
    followers_count : 1882097
    following : false
    friends_count : 680
    geo_enabled : false
    has_extended_profile : true
    id : 471672239
    id_str : "471672239"
    is_translation_enabled : false
    is_translator : false
    lang : "en"
    listed_count : 7544
    location : "Washington, DC"
    name : "Kellyanne Conway"
    notifications : false
    profile_background_color : "000000"
    profile_background_image_url : "http://abs.twimg.com/images/themes/theme1/bg.png"
    profile_background_image_url_https : "https://abs.twimg.com/images/themes/theme1/bg.png"
    profile_background_tile : false
    profile_banner_url : "https://pbs.twimg.com/profile_banners/471672239/1492471281"
    profile_image_url : "http://pbs.twimg.com/profile_images/854112636287451138/8S0FsJtV_normal.jpg"
    profile_image_url_https : "https://pbs.twimg.com/profile_images/854112636287451138/8S0FsJtV_normal.jpg"
    profile_link_color : "F58EA8"
    profile_location : {full_name: "Washington, DC", url: "https://api.twitter.com/1.1/geo/id/01fbe706f872cb32.json", country: "", place_type: "unknown", bounding_box: null, …}
    profile_sidebar_border_color : "000000"
    profile_sidebar_fill_color : "000000"
    profile_text_color : "000000"
    profile_use_background_image : false
    protected : false
    screen_name : "KellyannePolls"
    status : {contributors: null, truncated: true, text: "Passing #TaxCutsAndJobsAct in the House an importa…elief to job creators, j… https://t.co/jRhVgwELwC", is_quote_status: false, in_reply_to_status_id: null, …}
    statuses_count : 7223
    time_zone : null
    translator_type : "none"
    url : null
    utc_offset : null
    verified : true
  }
*/
