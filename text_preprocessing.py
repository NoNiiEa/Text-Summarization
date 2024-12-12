import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_data(data):
    texts = []
    for msg in data:
        texts.append(msg["full_text"])
    return texts

def text_processing(data):

    texts = clean_data(data)
    result = []

    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  
        u"\U0001F300-\U0001F5FF" 
        u"\U0001F680-\U0001F6FF" 
        u"\U0001F1E0-\U0001F1FF"  
        u"\U00002500-\U00002BEF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"
        u"\u3030"
        u"\u00f3"
                      "]+", re.UNICODE)
    translator = str.maketrans('', '', string.punctuation)
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    for text in texts:
        text = text.lower()
        text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
        text = re.sub(emoj, '', text)
        text = text.translate(translator)
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
        lemmas = [lemmatizer.lemmatize(word) for word in tokens]
        result.append(lemmas)
    return result