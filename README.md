# HackerEarthAssignment

#This Assignment targets at analyzing sentiments for a given Amazon product. 


#Step-1: Scraping Amazon Reviews using AmazonReviewScraper.ipynb file
	
	1. From product link page, identify and navigate to "All Reviews" link
	
	2. Identify specific tags containing relevant information required:
		
		a. Reviewer
		
		b. Date of Review
		
		c. Colour
		
		d. Size
		
		e. Verified Purchase (True or False)
		
		f. Rating
		
		g. Review Title
		
		h. Review Description
	
	3. Store all information in pandas.DataFrame object
	
	4. Transfer records to AmazonReviews.csv file
	
	

	Note: 
		
	i. Change/Edit proxies parameter in requestURL() to handle connection Timeout errors
	ii. Retries have been implemented with sleep time to handle url request errors or 'Tag not found' exceptions

#Step-2: Sentiment Analysis on Reviews Description

For Sentiment Analysis of this assignment, I have used CountVectorizer to convert normalized corpus to vectors and applied Multinomial NaiveBayes for classification on df['Rating'] due to high accuracy score between Multinomial Naive Bayes, Logistic Regression & Bernoulli Naive Bayes

		MultinomialNB | BernoulliNB | Logistic Regression
		=================================================
			0.72  |	   0.66	    |		0.68
		=================================================

In order to fit into [-1,1] range of sentiments:
	Ratings < '3' --> -1
	Ratings = '3' --> 0
	Ratings > '3' --> 1

Sentiment data is appended to reviews' DataFrame object which in turn is converted to sentimentAnalysis.json for further use

#Step-3: Building REST API over sentiment analysis json

Used Libraries: Django 2.1.7

REST API built on sentimentAnalysis.json: http://localhost:8000/filter/v1/applyfilter/

	1. If all requirements are fulfilled as per ecom_products/requirements.txt,
	   Run > python manage.py runserver
	   Wait till you see following message:
		Django version 2.1.7, using settings 'ecom_products.settings'
		Starting development server at http://127.0.0.1:8000/
		Quit the server with CONTROL-C

	2. Using POSTMAN, raise a GET request to http://localhost:8000/filter/v1/applyfilter/
		

REST API above can be used to filter reviews by colour, rating, sentiment, is_verified_purchase and sort by date ('asc', 'desc')
