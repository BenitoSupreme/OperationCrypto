# OperationCrypto
I'm trying to predict when Bitcoin prices will rise or fall. The branches in this repository use different algorithms to help me achieve my goal. 

OperationCryptoVol1: I used a regression tree to match different features (from a csv file I downloaded on kaggle using historic Bitcoin data) to the target variable, Bitcoin opening price. You'll also see that I graphed r squared value of my model to the depth of the decision tree. I used this to find the optimal decision tree depth. To further strengthen the restults I used cross validation to train my data for the R squared values.

ScrapeWiki: This doesn't relate to my main mission but was something I coded to get a wireframe to scrape a site... maybe I will delete this from this repo later

Scrape_Crypto_Site: Here I scraped an article from the popular crypto news site CoinDeck and tried different sentiment analysis. Textblob didn't work well, and because most of the results came up with a subjectivity score of 0 I concluded that this was a result of the OOV issue with some NLP algos. I then tried Vader library and got somewhat better results.

Next? I'm looking to make a bot that will click through multiple articles and scrape all of those. From there I'll be able to get an average sentiment score and then compare that value to the most recent articles sentiment score. This will give me a threshold for buying a currency or not. 


# MDL 
I gathered all the text from CoinDeck, and I am trying to run the data through sentiment library. ask me for the api Key. 

Scrapper: Gets the text contents from all the articles on coindeck, and saves the data from each sub url to a unique article called articlei.txt where i is enumerated. PROBLEM the data contains noise from the html. I think it would be better if I found the id for the contents of the article exclusively instead of gathering all text. I wonder if there is a news webscrapper already?

Senti.py: a call to open ai. exploring using openai to do sentiment. contact me for the key

