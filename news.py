from authpy import auth_kaggle
from zipfile import ZipFile
import pandas as pd


# loads db from kaggle and creates dataframe with the wanted columns from db
def load_kaggle():
    kaggle_api = auth_kaggle()
    # retrieve database from Kaggle
    kaggle_api.dataset_download_file('balabaskar/bitcoin-news-articles-text-corpora', file_name='bitcoin_articles.csv')

    # unzip kaggle database and save in this directory
    zf = ZipFile('bitcoin_articles.csv.zip')
    zf.extractall()
    zf.close()

    # load selected columns from db
    df = pd.read_csv('bitcoin_articles.csv', index_col=None, usecols=['title', 'author', 'summary',
                                                                      'published_date', 'link', 'article_rank'])

    # transform the 'published date' column from the database to date format and drop the column with object format
    published_date_change = df['published_date']
    published_date_change = pd.to_datetime(published_date_change).dt.date
    df = df.drop(columns=['published_date'])

    # merge the datetime format column with the rest of the table
    df = pd.concat([df, published_date_change], axis=1)
    return df


# selects the article to tweet
def select_article(table):
    table = load_kaggle()

    # select one random article with from the db that is ranked within the top 1000 articles
    table = table[table['article_rank'] < 1000]
    post = table.sample(n=1)
    title = post['title'].values[0]
    author = post['author'].values[0]
    link = post['link'].values[0]
    published_date = post['published_date'].values[0]
    description = post['summary'].values[0]
    return title, author, link, published_date, description

