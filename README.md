# Tweet_Automator

The repository is a Python-based program that scrapes Google for the top news article on bitcoin and performs several actions on it. The first step is to run a web scraping script that searches Google for the most recent news articles on bitcoin. Once the article is found, the program then breaks it down into its main components, such as the title, author, publication date, and body text.

The next step is to save the article to a SQL database. If the article was found through the Google search, it will be saved in a database specifically for Google articles. However, if the program is unable to find an article through Google, it will automatically download a database of articles related to bitcoin from Kaggle and search through that database for the most recent news article. In this case, the article will be saved in a different SQL database specifically for Kaggle articles.

Finally, the program will tweet the article from the owner's Twitter account, using the Twitter API. The tweet will include a shortened URL to the full article, the title, and a brief summary of the article's content.

This repository is useful for anyone who wants to stay up-to-date on the latest news about bitcoin and wants to automate the process of finding, storing, and sharing news articles with others. The program can be run on a regular basis, such as daily or hourly, to ensure that the latest news is always available in the database and shared on the owner's Twitter account.

# Dependencies
Python 3.6 or higher
Tweepy
Beautiful Soup
SQLAlchemy

# Installation and Usage
- Clone the repository to your local machine.
- Install the dependencies using pip: pip install -r requirements.txt
- Create a PostgreSQL database and update the database connection details in creds.json. You will most likely need the following credentials to enable this connection:
  -   db_host
  -   db_name
  -   db_user (If database is set up to require it)
  -   db_pass (If database is set up to require it)
  -   port_id
- Set up a Twitter Developer account and get API keys. There are multiple, very well documented tutorials to set this up.
- Set up a PostgreSQL database and update the database connection details in creds.json or config.py. Note: If you do decide to use config.py instead of creds.json, make sure to edit the credentials paths in the following files:
  - sql_conn.py
  - main.py
  - authpy.py
- Run the program using python main.py.
- The program will automatically search for the latest bitcoin news article and tweet it from the owner's Twitter account.
- Extra: You can use PGAdmin4 as the GUI to interact with your PostgreSQL database. Personal recommendation.
- This repository is useful for anyone who wants to stay updated on the latest news about bitcoin and automate the process of finding, storing, and sharing news articles with others.

Additionally, would like to give recognition to the kaggle dataset owner that was used in this project as an example. Owner: balabaskar Dataset: bitcoin-news-articles-text-corpora
