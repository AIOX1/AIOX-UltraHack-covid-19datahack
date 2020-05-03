### DISCLAIMER
### Due to IP reasons we had to edit out the code files to remove sensitive information.
### We explain the methods but this code file cannot be run as is

from aiox import tokenize, compute_tf, compute_idf_enqueue, vectorizer, register_vector

#we use a mix of TFIDF analysis, and articles vectorization with later analysis on the latent
#space of articles vectors

#We have an internal TF-IDF analyzer
def tfidf(article_text, article_id):
    tokens = tokenize(article_text)
    for token in tokens:
        #for each term we compute tf score
        compute_tf(token)
        #we then schedule idf computations on our infrastructure
        compute_idf_enqueue(token, article_id)

def vectorize(article_text, article_id):
    #we turn the article into a numbers vector
    vector = vectorizer(article_text)
    #we register the vector in our database
    register_vector(vector, article_id)
