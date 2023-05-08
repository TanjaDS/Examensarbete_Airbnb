
# Airbnb Stockoholm NLP Project

This is a project analyzing Airbnb listings in Stockholm using NLP techniques.

# Notebooks

The notebooks should be run in the following order:
1. transformation_and_EDA/data_cleaning.ipynb: This notebook cleans the data by removing unnecessary symbols from texts, performing text preprocessing, filling missing values, and converting data types. The cleaned data is saved in the staging_data folder.
2. models/sentiment_analysis.ipynb: This notebook labels the reviews as negative or positive using nltk SentimentIntensityAnalyzer.
3. models/topic_modelling.ipynb: This notebook trains a model to find topics in all the data using gensim.ldamodel.
4. models/topic_modelling_neg.ipynb: This notebook trains a model to find topics in the data labeled as negative reviews using gensim.ldamodel.
5. transformation_and_EDA/EDA.ipynb: This notebook performs exploratory data analysis on the cleaned data and generates visualizations to gain insights.

Other notebooks can be run after in any order.

# Data

The data source http://insideairbnb.com/get-the-data.
The data is stored in the different folders. The raw data is stored in raw_data, the cleaned data is stored in staging_data, and trained data is stored in processed_data.

# Dependencies

This project requires the libraries to be installed. Run setup.yml to create a conda env with all dependecies. 

# Author

Tatiana Ilyasova, EC Utbildning, DS21