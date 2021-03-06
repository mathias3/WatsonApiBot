import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

def analyze(handle):
	twitter_consumer_key= ''
	twitter_consumer_secret= ''
	twitter_access_token= ''
	twitter_access_token_secret= ''
	
	twitter_api = twitter.Api(consumer_key=twitter_consumer_key, 			consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)


	statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)
	text = ""
	for status in statuses:
            if (status.lang =='en'): #English tweets
                    text += status.text.encode('utf-8')
