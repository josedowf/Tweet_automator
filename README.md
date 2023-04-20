# Tweet_Automator

The repository is a Python-based program that scrapes Google for the top news article on bitcoin and performs several actions on it. The first step is to run a web scraping script that searches Google for the most recent news articles on bitcoin. Once the article is found, the program then breaks it down into its main components, such as the title, author, publication date, and body text.

The next step is to save the article to a SQL database. If the article was found through the Google search, it will be saved in a database specifically for Google articles. However, if the program is unable to find an article through Google, it will automatically download a database of articles related to bitcoin from Kaggle and search through that database for the most recent news article. In this case, the article will be saved in a different SQL database specifically for Kaggle articles.

Finally, the program will tweet the article from the owner's Twitter account, using the Twitter API. The tweet will include a shortened URL to the full article, the title, and a brief summary of the article's content.

This repository is useful for anyone who wants to stay up-to-date on the latest news about bitcoin and wants to automate the process of finding, storing, and sharing news articles with others. The program can be run on a regular basis, such as daily or hourly, to ensure that the latest news is always available in the database and shared on the owner's Twitter account.