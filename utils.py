from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

def csv_reader():
    text = open('D:\Developments\Python\src\Pemrosesan Data Multimedia\Data Text Processing\Dataset\dataset_text.csv')
    text = ' '.join(i for i in text)
    return text

def convert_lowercase(s=""):
    new_s = s.lower()
    return new_s

def stop_word_removal(tokenize_word):
    more_stopword = ['aku', 'kamu', 'sini', 'kau', 'apa', 'bagaimana']
    stop_word_factory = StopWordRemoverFactory()
    stop_words = stop_word_factory.get_stop_words() + more_stopword
    words = [w for w in tokenize_word if not w.lower() in stop_words]
    words = []
    
    for w in tokenize_word:
        if w not in stop_words:
            words.append(w)
    return words