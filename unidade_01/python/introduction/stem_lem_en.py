import spacy

# spaCy para portugues
nlp = spacy.load("en_core_web_sm")

# Frase de exemplo
text = "I was swimming in the river during the summer"

# Lemmatização com spaCy
doc = nlp(text)
lemmatized_words = [token.lemma_ for token in doc]
print("Lemmatization (spaCy):", lemmatized_words)


from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

# Frase de exemplo
frase = "I swam across the river during the summer"

# Dividir a frase em palavras
palavras = frase.split()

# Aplicar stemming a cada palavra
stemmed_palavras = [stemmer.stem(palavra) for palavra in palavras]

# Reunir as palavras em uma frase novamente
frase_stemmed = ' '.join(stemmed_palavras)

# Exibir a frase com stemming
print("Stemming (SnowballStemmer):", frase_stemmed)

