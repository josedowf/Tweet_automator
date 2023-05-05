from authpy import auth_twitter
from utils import my_time, home_time, check_duplicate_article_from_kaggle, check_duplicate_article_from_google
from news import load_kaggle, select_article
from sql_conn import load_google_article_to_sql, load_kaggle_article_to_sql
from web_scraper import scraped_article

# access the Twitter API
twitter_api = auth_twitter(r'/Users/josedow/PycharmProjects/Tweet_automator/creds.json')

# Google search text
google_search = 'DeFi news today'

if scraped_article(google_search) != 'Error':
    # scrape google for a new article about Bitcoin
    post = scraped_article(google_search)
    print("Selected an article from Google News!")
    print()
    # verifies against SQL database if post is a duplicate
    check_duplicate = check_duplicate_article_from_google(post)
    # load tweet to sql db
    load_google_article_to_sql(post)
    print()
else:
    # retrieves the post selected from Kaggle database
    post = select_article(load_kaggle())
    print("Selected an article from Kaggle database!")
    print()
    # verifies against SQL database if post is a duplicate
    check_duplicate = check_duplicate_article_from_kaggle(post)

    # loop that keeps pulling articles until pick is not a duplicate
    while check_duplicate != 0:
        # retrieves a new post selected from database
        post = select_article(load_kaggle())

        # verifies against SQL database if post is a duplicate
        check_duplicate = check_duplicate_article_from_kaggle(post)
        print("The article selected was already posted... Picking a new one!")
        print()
    else:
        print("Article selected has not been tweeted before!")
        print()
        load_kaggle_article_to_sql(post)
        print()

# breaks down selected post into its main components
title = post[0]
author = post[1]
link = post[2]
published_date = post[3]
description = post[4]

# what wil be tweeted
tweet_content = f"{title}\n -{author}\n Published: {published_date}\n{link}"

# log message
print('The chosen article for today:')
print(tweet_content)
print(f'Article info: {description}')
print()


# function that posts the tweet
twitter_api.update_status(tweet_content)

print("Successfully Tweeted!")
print()
print(f"Tweeted at: {my_time()}")
print(f"At Navojoa, the time was: {home_time()}")
