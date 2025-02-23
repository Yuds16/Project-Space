from keybert import KeyBERT

# Initialize the KeyBERT model
model = KeyBERT('distilbert-base-nli-mean-tokens')

# Example text
text = """
         Transformers provides thousands of pre-trained models to perform tasks on texts such as classification, 
         information extraction, question answering, summarization, translation, text generation, etc. 
         Each architecture is designed with a specific task in mind.
       """

# Extract keywords
keywords = model.extract_keywords(text)

# Print the keywords
print("Keywords:")
for keyword in keywords:
    print(keyword)