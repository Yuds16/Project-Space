import spacy
import pytextrank

from pdf_reader import PDFReader

fname = "sample/sample.pdf"

# python3 -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")
pdf_reader = PDFReader(fname)
doc = nlp(pdf_reader.read_pdf())

# examine the top-ranked phrases in the document
for phrase in doc._.phrases:
    print(phrase.text)