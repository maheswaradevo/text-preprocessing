import nltk
import string
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def csv_reader():
    text = open('D:\Developments\Python\src\Pemrosesan Data Multimedia\Data Text Processing\Dataset\dataset_text.csv')
    text = ' '.join(i for i in text)
    return text

def convert_lowercase(s=""):
    new_s = s.lower()
    return new_s

def stem_words(s, word_tokenize):
    doc = s
    stem_factory = StemmerFactory()
    stemmer = stem_factory.create_stemmer()
    doc = [stemmer.stem(word_tokenize) for sentence in doc for word_tokenize in sentence.split(" ")]
    return doc

def stop_words_removal(s):
    s = s.translate(str.maketrans('','',string.punctuation)).lower()
    tokens = word_tokenize(s)
    list_stop_words = set(stopwords.words('indonesian'))

    removed = []
    for t in tokens:
        if t not in list_stop_words:
            removed.append(t)
    return removed

def remove_duplicate(s):
    s = list(dict.fromkeys(s))
    return s
