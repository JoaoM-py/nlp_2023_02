import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import numpy as np
from gensim.models import Word2Vec
from nltk.corpus import stopwords
stop_words = set(stopwords.words('portuguese') + list(string.punctuation))
stop_words.remove('não')

# Carregando um modelo Word2Vec pré-treinado
model = Word2Vec.load('./model_word2vec.model')

def rewrite_sentence(sentence, model):
    tokens = preprocess_text(sentence)
    rewritten_tokens = [find_synonym(token, model) for token in tokens]
    rewritten_sentence = ' '.join(rewritten_tokens)
    return rewritten_sentence

def find_synonym(word, model):
    try:
        # sinônimos com base na similaridade de palavras
        synonyms = model.wv.most_similar(word, topn=1)
        return synonyms[0][0]
    except KeyError:
        return word

def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return tokens




user_input = input("Digite uma frase: ")
rewritten_sentence = rewrite_sentence(user_input, model)
print("Frase Original:", user_input)
print("Frase Reescrita:", rewritten_sentence)