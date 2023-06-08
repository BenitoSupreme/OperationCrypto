# OperationCrypto
I'm trying to predict when Bitcoin prices will rise or fall. The branches in this repository use different algorithms to help me achieve my goal. 

OperationCryptoVol1: I used a regression tree to match different features (from a csv file I downloaded on kaggle using historic Bitcoin data) to the target variable, Bitcoin opening price. You'll also see that I graphed r squared value of my model to the depth of the decision tree. I used this to find the optimal decision tree depth. To further strengthen the restults I used cross validation to train my data for the R squared values.

ScrapeWiki: This doesn't relate to my main mission but was something I coded to get a wireframe to scrape a site... maybe I will delete this from this repo later

Scrape_Crypto_Site: Here I scraped an article from the popular crypto news site CoinDeck and tried different sentiment analysis. Textblob didn't work well, and because most of the results came up with a subjectivity score of 0 I concluded that this was a result of the OOV issue with some NLP algos. I then tried Vader library and got somewhat better results.

Next? I'm looking to make a bot that will click through multiple articles and scrape all of those. From there I'll be able to get an average sentiment score and then compare that value to the most recent articles sentiment score. This will give me a threshold for buying a currency or not. 
