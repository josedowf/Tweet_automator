import tweepy
import json
from kaggle.api.kaggle_api_extended import KaggleApi


# auth function for Twitter
def auth_twitter(creds: str = r'/Users/josedow/PycharmProjects/Tweet_automator/creds.json'):

    # Authenticate to Twitter and get API object.
    creds = read_creds(creds)
    api_key, api_secret = creds['api_key'], creds['api_secret']
    tk, tk_secrets = creds['access_token'], creds['access_secret']

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(tk, tk_secrets)

    # Create the API object
    api_auth = tweepy.API(auth, wait_on_rate_limit=True)
    return api_auth


# auth function for Kaggle
def auth_kaggle():
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()
    return kaggle_api


# read credentials from creds.json file
def read_creds(filename):
    # Read JSON file to load credentials.
    # Store API credentials in a safe place.
    # If you use Git, make sure to add the file to .gitignore
    with open(filename) as f:
        creds = json.load(f)
    return creds


# test if Twitter api is working
if __name__ == '__main__':
    credentials = r'/Users/josedow/PycharmProjects/Tweet_automator/creds.json'
    api_twitter = auth_twitter(credentials)

    # Try auth access
    try:
        api_twitter.verify_credentials()
        print('Successful Twitter Authentication')
    except Exception as error:
        print('Failed Twitter authentication')
        print(error)


# test if Kaggle api is working
if __name__ == '__main__':
    credentials = r'/Users/josedow/PycharmProjects/Tweet_automator/creds.json'
    api_kaggle = auth_kaggle()

    # Try auth access
    try:
        api_kaggle.authenticate()
        print('Successful Kaggle Authentication')
    except Exception as error:
        print('Failed Kaggle authentication')
        print(error)
