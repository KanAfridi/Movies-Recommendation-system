# Movie Recommendation System 🎥  

This project is focused on recommending movies using data obtained from the TMDb API. The dataset contains approximately 10,000 movies, providing a rich resource for building a recommendation system.  

## Project Overview 🔍

This application allows users to select a movie and receive **5 similar movies** based on the selected title.  

To achieve this, I have implemented a variety of machine learning techniques, including:  

### Text Preprocessing 🛠️
To prepare the data for the model, I cleaned and processed it extensively. The raw data included a large number of list-format entries, which required custom techniques and functions to extract and format the relevant information.

- Converted text to lowercase 
- Removed punctuation 
- Eliminated stopwords   
- Tokenization and Lemmatization   
  - Tokenized the text into meaningful units.  
  - Applied lemmatization for better semantic representation.  
---
### Machine Learning Techniques 🔩⚙️
1. **Stemming:**
    - Stemming to reduce words to their base or root form by removing prefixes or suffixes

2. **Bag of Words (BoW):**
    - This technique is used to convert textual data into numerical vectors, making it suitable for use in machine learning models.

    - ***CountVectorizer***: 
        - Text data was transformed into a format suitable for machine learning models using CountVectorizer.  
        - This process represented text numerically, emphasizing the importance of words relative to the dataset.  

3. **Cosine Similarity:**
    - Cosine Similarity is a measure used to determine how similar two text documents (or vectors) are, by calculating the cosine of the angle between them.

## Key Features  

- A dataset of 10,000 movies from TMDb API 🎞️  
- Advanced data cleaning and preprocessing 🧹  
- Text vectorization using Bag of Words 📊  
- Recommendation of 5 similar movies based on user selection 🤖  

## How It Works  

1. The raw data is cleaned to extract relevant information from complex formats like lists.  
2. Textual data is transformed into numerical vectors using the Bag of Words technique.  
3. A similarity model predicts and recommends 5 movies that are most similar to the selected one.  

---

This project showcases my ability to handle large datasets, preprocess complex data, and apply machine learning techniques for creating a user-friendly recommendation system.  
