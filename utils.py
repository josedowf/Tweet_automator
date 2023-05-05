from datetime import datetime
from sql_conn import previous_tweets_from_google, previous_tweets_from_kaggle
import numpy as np
import pytz


# gives the current time from where I currently am
def my_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time


# gives the current time in Navojoa
def home_time():
    tz_her = pytz.timezone('America/Hermosillo')
    home = datetime.now(tz_her).strftime("%H:%M:%S")
    return home


def check_duplicates_fn(new_tweets_list):
    checklist = set()
    for elem in new_tweets_list:
        if elem in checklist:
            return 1
        else:
            checklist.add(elem)
    return 0


# append the new article to the tweets list and verify if it's a duplicate
def check_duplicate_article_from_kaggle(article):
    tweets = previous_tweets_from_kaggle()
    new_tweets_list = np.append(article, tweets)
    result = check_duplicates_fn(new_tweets_list)
    return result


def check_duplicate_article_from_google(article):
    tweets = previous_tweets_from_google()
    new_tweets_list = np.append(article, tweets)
    result = check_duplicates_fn(new_tweets_list)
    return result





