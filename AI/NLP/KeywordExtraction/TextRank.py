import spacy
import pytextrank

# example text
text = "TextRank is a keyword extraction algorithm based on PageRank and has been widely used in natural language processing tasks."

# load a spaCy model, depending on language, scale, etc.
# python3 -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")
doc = nlp(text)

# examine the top-ranked phrases in the document
for phrase in doc._.phrases:
    print(phrase.text)