def csv_reader():
    text = open('D:\Developments\Python\src\Pemrosesan Data Multimedia\Data Text Processing\Dataset\dataset_text.csv')
    text = ' '.join(i for i in text)
    return text