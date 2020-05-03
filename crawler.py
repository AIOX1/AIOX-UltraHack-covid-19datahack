### DISCLAIMER
### Due to IP reasons we had to edit out the code files to remove sensitive information.
### We explain the methods but this code file cannot be run as is

import requests
from aiox import links_selector, text_cleaner, sentences_selector

#NOTE: we develop our own crawler, for scalability reasons.
# We need to perform massive crawling on many sources, every hour.

def fetchLinksFromURL(url):
    #we fetch the HTML code from each news media homepage
    #we then detect all the new links (articles) and store those for later crawling
    try:
        r = requests.get(url)
    except requests.exceptions.Timeout:
        return
    html = r.text
    #we fetch links
    soup = BeautifulSoup(html)
    links = soup.findAll('a')
    #Here we use a internal deep learning classification neural network
    #to keep only links that are most likely newly released press articles
    true_links = links_selector(links)
    return true_links

def fetchArticleFromURL(url):
    try:
        r = requests.get(url)
    except requests.exceptions.Timeout:
        return
    html = r.text
    #we apply a first cleaning step to remove easy to spot garbage patterns such as
    #characters sequences that are too long without whitespace etc
    clean_text = text_cleaner(html)
    #Then we use a proprietary deep learning classification network to extract only sentences
    # = seem to have a subject, verb, and a meaning
    clean_sentences = sentences_selector(clean_text)
    return clean_sentences
