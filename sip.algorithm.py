
import nltk
from nltk import bigrams
from nltk.corpus import stopwords
from collections import Counter, defaultdict
import re
import requests

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to download and return the content of a text file from a URL
def download_text(url):
    response = requests.get(url)
    return response.text

# Function to preprocess the text (remove headers, footers, and other non-relevant parts)
def preprocess_text(text):
    # Gutenberg texts often have a standard header and footer that can be removed by slicing
    # The actual content usually starts with "*** START" and ends with "*** END"
    start = text.find("*** START")
    end = text.find("*** END")
    return text[start:end]

# URL of the book
book_url = 'data/data.txt'

# Download and preprocess the text
raw_text = download_text(book_url)
processed_text = preprocess_text(raw_text)

# Tokenize and create bigrams for the document
stop_words = set(stopwords.words('english'))
words = nltk.word_tokenize(processed_text.lower())
filtered_words = [word for word in words if word not in stop_words and word.isalnum()]
bigrams_list = list(nltk.bigrams(filtered_words))

# Calculate bigram frequencies across the document
collection_freq = Counter(bigrams_list)

# Expected frequency (in this case, equal to actual frequency as we have one document)
doc_expected_freq = {bigram: freq for bigram, freq in collection_freq.items()}

# Identify SIPs in the document
sip_threshold = 0.9  # Adjust this threshold as needed
sips = [bigram for bigram, freq in collection_freq.items() if freq > doc_expected_freq[bigram] * sip_threshold]

# Output SIPs for the document
print("Statistically Improbable Phrases (SIPs):")
for sip in sips:
    print(' '.join(sip))
