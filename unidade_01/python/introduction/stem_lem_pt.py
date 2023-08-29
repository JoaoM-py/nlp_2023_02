import spacy

# Load the spaCy model for Portuguese
nlp = spacy.load("pt_core_news_sm")

# Text to process
text = "Eu estava correndo por aí"

# Lemmatization with spaCy
doc = nlp(text)
lemmatized_words = [token.lemma_ for token in doc]
print("Lemmatization (spaCy):", lemmatized_words)


from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("portuguese")

# Frase de exemplo
frase = "Eu corri pelo parque"

# Dividir a frase em palavras
palavras = frase.split()

# Aplicar stemming a cada palavra
stemmed_palavras = [stemmer.stem(palavra) for palavra in palavras]

# Reunir as palavras em uma frase novamente
frase_stemmed = ' '.join(stemmed_palavras)

# Exibir a frase com stemming
print("Stemming (SnowballStemmer):", frase_stemmed)

