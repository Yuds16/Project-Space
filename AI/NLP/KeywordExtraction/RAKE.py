import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
from rake_nltk import Rake

# Create a Rake instance
r = Rake()

# Text from which keywords will be extracted
text = "RAKE (Rapid Automatic Keyword Extraction) is a keyword extraction algorithm that automatically identifies relevant keywords and phrases in a text document."

# Extract keywords from the text
r.extract_keywords_from_text(text)

# Get the ranked keywords
keywords = r.get_ranked_phrases_with_scores()

# Print the extracted keywords and their scores
for score, kw in keywords:
    print("Keyword:", kw, "Score:", score)