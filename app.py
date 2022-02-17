import utils
from nltk.tokenize import sent_tokenize, word_tokenize

document = ""
document = utils.csv_reader()
new_document = utils.convert_lowercase(document)

# Tokenizing document that are given per words.
words = word_tokenize(new_document)
new_words = [text for text in words if text.isalnum()]
print("WORDS")
print(new_words)

print("============================")

# Tokenizing document that are given per sentences.
print("SENTENCES")
sentences = sent_tokenize(new_document)
print(sentences)

print("============================")

# Removing stop words in indonesian language
print("STOP WORDS REMOVAL")
filtering = utils.stop_word_removal(new_words)
print(filtering)