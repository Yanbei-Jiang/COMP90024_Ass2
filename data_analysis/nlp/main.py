import json
from sentiment_polarity import *
#from topic_extraction import *

def old_tweet_analysis(tweet_obj):
    text = tweet_obj["doc"]["text"]
    return process_tweet(text)


def new_tweet_analysis(tweet_obj):
    for key in tweet_obj.keys():
        # only look at the third key (i.e. "Hoppers_Crossing_1522304716188700672_stream")
        if tweet_obj[key] != "_id" and tweet_obj[key] != "_rev":
            if "extended_tweet" in tweet_obj[key].keys():
                text = tweet_obj[key]["extended_tweet"]["full_text"]
            else:
                text = tweet_obj[key]["text"]
    return process_tweet(text)


def process_tweet(text):
    processed_text = preprocess(text)
    sentiment = sentiment_analysis(processed_text)
    tweet_obj["sentiment"] = sentiment
    polarity = polarity_analysis(processed_text)
    tweet_obj["polarity"] = polarity
    return tweet_obj


def preprocess(text):
    new_text = []
    for t in text.split(" "):
        if not t.startswith('@') and not t.startswith('http'):
            new_text.append(t)
    
    return " ".join(new_text)



tweet_obj = {
  "_id": "46973e57e0ea61f4ebe9294bd0019dd3",
  "_rev": "1-4318f424f7fa313c7c19b0726eb4aa51",
  "id": "495069053614960640",
  "key": [
    "melbourne",
    2014,
    8,
    1
  ],
  "value": 1,
  "doc": {
    "_id": "495069053614960640",
    "_rev": "1-9de94949b497fb6027d1aedf5960d3ea",
    "contributors": "null",
    "truncated": "false",
    "text": "@tehbebe @FraserWJ @AussieHobbit we are dancing to this tomorrow night!",
    "in_reply_to_status_id": 495060696099332100,
    "id": 495069053614960640,
    "favorite_count": 0,
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "retweeted": "false",
    "coordinates": {
      "type": "Point",
      "coordinates": [
        145.06180664,
        -37.84985396
      ]
    },
    "entities": {
      "symbols": [],
      "user_mentions": [
        {
          "id": 618994513,
          "indices": [
            0,
            8
          ],
          "id_str": "618994513",
          "screen_name": "tehbebe",
          "name": "Bebe Sammiie"
        },
        {
          "id": 837713052,
          "indices": [
            9,
            18
          ],
          "id_str": "837713052",
          "screen_name": "FraserWJ",
          "name": "Fraser (Fray Fray)"
        },
        {
          "id": 23743664,
          "indices": [
            19,
            32
          ],
          "id_str": "23743664",
          "screen_name": "AussieHobbit",
          "name": "Rhianna"
        }
      ],
      "hashtags": [],
      "urls": []
    },
    "in_reply_to_screen_name": "tehbebe",
    "in_reply_to_user_id": 618994513,
    "retweet_count": 0,
    "id_str": "495069053614960640",
    "favorited": "false",
    "user": {
      "follow_request_sent": "false",
      "profile_use_background_image": "true",
      "default_profile_image": "false",
      "id": 700505767,
      "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
      "verified": "false",
      "profile_text_color": "333333",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/2405138431/1338817_2068372_normal.jpg",
      "profile_sidebar_fill_color": "DDEEF6",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "https://t.co/DumFSsUdXx",
              "indices": [
                0,
                23
              ],
              "expanded_url": "https://www.youtube.com/user/maizey108",
              "display_url": "youtube.com/user/maizey108"
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "followers_count": 174,
      "profile_sidebar_border_color": "C0DEED",
      "id_str": "700505767",
      "profile_background_color": "C0DEED",
      "listed_count": 6,
      "is_translation_enabled": "false",
      "utc_offset": 36000,
      "statuses_count": 2317,
      "description": "Actor and YouTube Vlogger/gamer. I have a terribly short attention span so that may change in about 2 sec- oh look! something shiny!",
      "friends_count": 192,
      "location": "Melbourne",
      "profile_link_color": "FA7DBF",
      "profile_image_url": "http://pbs.twimg.com/profile_images/2405138431/1338817_2068372_normal.jpg",
      "following": "false",
      "geo_enabled": "true",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/700505767/1391333438",
      "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
      "screen_name": "Maizey108",
      "lang": "en",
      "profile_background_tile": "false",
      "favourites_count": 302,
      "name": "LukaOnline",
      "notifications": "false",
      "url": "https://t.co/DumFSsUdXx",
      "created_at": "Tue Jul 17 06:28:54 +0000 2012",
      "contributors_enabled": "false",
      "time_zone": "Melbourne",
      "protected": "false",
      "default_profile": "false",
      "is_translator": "false"
    },
    "geo": {
      "type": "Point",
      "coordinates": [
        -37.84985396,
        145.06180664
      ]
    },
    "in_reply_to_user_id_str": "618994513",
    "lang": "en",
    "created_at": "Fri Aug 01 04:50:34 +0000 2014",
    "in_reply_to_status_id_str": "495060696099332096",
    "place": {
      "full_name": "Melbourne",
      "url": "https://api.twitter.com/1.1/geo/id/01864a8a64df9dc4.json",
      "country": "Australia",
      "place_type": "city",
      "bounding_box": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              144.593741856,
              -38.433859306
            ],
            [
              145.512528832,
              -38.433859306
            ],
            [
              145.512528832,
              -37.5112737225
            ],
            [
              144.593741856,
              -37.5112737225
            ]
          ]
        ]
      },
      "contained_within": [],
      "country_code": "AU",
      "attributes": {},
      "id": "01864a8a64df9dc4",
      "name": "Melbourne"
    },
    "metadata": {
      "iso_language_code": "en",
      "result_type": "recent"
    },
    "location": "melbourne"
  }
}

print(old_tweet_analysis(tweet_obj))