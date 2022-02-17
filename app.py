from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from utils import csv_reader

document = ""
document = csv_reader()

words = word_tokenize(document)
new_words = [text for text in words if text.isalnum()]

print("WORDS")
print(new_words)

print("============================")

print("SENTENCES")
sentences = sent_tokenize(document)

print(sentences)