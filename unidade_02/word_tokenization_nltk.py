import nltk
from nltk.tokenize import regexp_tokenize

frase = 'Tornar o futuro seguro e Próspero, conectando ciência e Tecnologia!'

#Frase retirando espaços
tokenizacao1 = regexp_tokenize(frase, r'\s+', gaps=True)

#Frase selecionando caracter maiúsculo 
tokenizacao2 = regexp_tokenize(frase, r'[A-Z]\w+')

print(tokenizacao1)
print('---------------------------------------------------------')
print(tokenizacao2)