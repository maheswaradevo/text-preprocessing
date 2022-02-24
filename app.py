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
filtering = utils.stop_words_removal(new_document)
print(filtering)

print("============================")

# Stemming the words
print("STEMMING")
stem = utils.stem_words(filtering, new_words)
print(stem)

print("============================")

# Removing duplicate
print("DUPLICATE REMOVAL")
duplicate_removal = utils.remove_duplicate(stem)
print(duplicate_removal)

print("============================")