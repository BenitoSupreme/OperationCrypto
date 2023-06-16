# OperationCrypto
I'm trying to predict when Bitcoin prices will rise or fall. The branches in this repository use different algorithms to help me achieve my goal. 

OperationCryptoVol1: I used a regression tree to match different features (from a csv file I downloaded on kaggle using historic Bitcoin data) to the target variable, Bitcoin opening price. You'll also see that I graphed r squared value of my model to the depth of the decision tree. I used this to find the optimal decision tree depth. To further strengthen the restults I used cross validation to train my data for the R squared values.

ScrapeWiki: This doesn't relate to my main mission but was something I coded to get a wireframe to scrape a site... maybe I will delete this from this repo later

Scrape_Crypto_Site: Here I scraped an article from the popular crypto news site CoinDeck and tried different sentiment analysis. Textblob didn't work well, and because most of the results came up with a subjectivity score of 0 I concluded that this was a result of the OOV issue with some NLP algos. I then tried Vader library and got somewhat better results.

gets_compound_score_of_article.py is the most recent addition and really ties everything together. I made three main functions. One is to scrape a site on coindesk and return the average sentiment score of that article. The second is to grab all of the hrefs from a main site page and return them in a list. The third (not created yet) will be to take that list of hrefs, shove each element into the average sentiment score function, and then average out all of the averages. This will give me a baseline threshold for a 'yes or know buy'

After I get this working, instead of doing an overall average I'm going to try and link the threshold  with the current trend of bitcoin (going up or down). I will also work on providing better data from my scrapers through more rigerous preprocessing. 
