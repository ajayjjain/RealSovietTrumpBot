from twython import Twython
import json
import goslate
import time
from transliterate import translit, get_available_language_codes


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
result = api.show_user(screen_name='realdonaldtrump')
tweet = result['status']['text']

while True:
    result = api.show_user(screen_name='realdonaldtrump')
    current_tweet = result['status']['text']
    if (current_tweet != tweet):
        translated_tweet = translit(current_tweet, 'ru')
        if len(translated_tweet) > 140:
            translated_tweet = translated_tweet[:139]
        api.update_status(status = translated_tweet)
        tweet = current_tweet
    time.sleep(10)
