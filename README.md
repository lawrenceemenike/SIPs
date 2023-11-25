# SIPs
A Python tool to identify statistically improbable phrases (SIPs) in text corpora, using natural language processing. This project automates the extraction of unique phrases, offering valuable insights for text analysis and data mining enthusiasts

# Dataset
This project uses a text dataset sourced from Project Gutenberg. The specific text used for analysis is available at the following URL: [https://www.gutenberg.org/ebooks/72210](https://www.gutenberg.org/ebooks/72210).

The text has been processed and included in the `data` directory under the filename `data.txt` for ease of access and analysis within the project.

# Preprocessing
The text dataset from Project Gutenberg typically includes headers and footers with information that is not part of the original book content. For the purpose of this analysis, the following preprocessing steps were applied to the dataset:

Header and Footer Removal: The text from Project Gutenberg contains standardised headers and footers that were removed to isolate the main content of the book. This was achieved by identifying specific markers that denote the start and end of the actual book content (e.g., "*** START" and "*** END").
Lowercasing and Tokenization: The text was converted to lowercase and then tokenized into words for further processing.
Stopword Removal and Filtering: Common English stopwords were removed, and only alphanumeric words were kept to ensure the analysis focuses on meaningful content.
These preprocessing steps are critical in ensuring that the analysis focuses on the core textual content of the book.

# Disclaimer
This project's use of the dataset from Project Gutenberg adheres to Project Gutenberg's terms and conditions. The dataset is used for educational and demonstration purposes within the scope of this project. Users of this project are encouraged to familiarize themselves with Project Gutenberg's terms of use, available at Project Gutenberg's website. The project does not redistribute the dataset but provides a link to the original source for access.
