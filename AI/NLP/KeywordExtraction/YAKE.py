from yake import KeywordExtractor

# Create a KeywordExtractor instance
kw_extractor = KeywordExtractor()

# Text from which keywords will be extracted
text = "YAKE (Yet Another Keyword Extractor) is a Python library for extracting keywords from text."

# Extract keywords from the text
keywords = kw_extractor.extract_keywords(text)

# Print the extracted keywords and their scores
for kw in keywords:
    print("Keyword:", kw[0], "Score:", kw[1])