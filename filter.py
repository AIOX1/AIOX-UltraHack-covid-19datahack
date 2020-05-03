### DISCLAIMER
### Due to IP reasons we had to edit out the code files to remove sensitive information.
### We explain the methods but this code file cannot be run as is

from aiox import text_segmenter, pg_classifier

#At this stage, the text is clean from the most obvious garbage patterns, and we have to filter out
#more subtle noise, such as for instance article comments, or website legal footer at the bottom
#of the page etc
def noiseFilter(rawText):
    #we extract paragraphs of sentences
    paragraphs = text_segmenter(rawText)
    #we keep only paragraphs that seem to have actual meaning related to article title
    meaningful_pgs = pg_classifier(paragraphs)
    return meaningful_pgs
