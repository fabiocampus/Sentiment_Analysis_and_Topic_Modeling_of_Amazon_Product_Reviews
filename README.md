# Sentiment_Analysis_and_Topic_Modeling_of_Amazon_Product_Reviews

This academic project aims to perform a sentiment analysis on Amazon reviews of various products belonging to 
different classes, and subsequently, the topic modeling on positive and negative reviews for each product, in 
order to identify the relevant characteristics, both positive and negative, within each product class. 
To gather data for the study, all the reviews were scrapped from Amazon. Different sentiment classifiers 
were, then, applied on the data to observe the most accurate classifier for the study. 
We used the best model to classify the data, and then we applied the LDA method for topic modeling. 
The study concluded that the most accurate sentiment classifier was GPT-3.5, tested on a pre-polarized 
dataset, in order to evaluate its performance. However, the limited use of its free API did not allow us to 
classify our Amazon reviews dataset. Therefore, the logistic regression classifier with an accuracy of 0.9362 
– trained on a sample of 400000 Amazon reviews pre-polarized – was selected for the project to polarize the 
dataset. Finally, the LDA method for topic modeling was applied to each product for both positive and 
negative reviews, visualizing the results via the pyLDAvis library, to create an interactive and more accurate 
visualization.
