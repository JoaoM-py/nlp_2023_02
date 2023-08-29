import nltk
import spacy
import numpy as np
import pandas as pd
import copy as cp
import joblib

sentence = """"Três dias depois, numa expansão íntima com o boticário Crispim Soares,
desvendou o alienista o mistério do seu coração.
—A caridade, Sr. Soares, entra decerto no meu procedimento, mas entra
como tempero, como o sal das coisas, que é assim que interpreto o dito de São Paulo
aos Coríntios: "Se eu conhecer quanto se pode saber, e não tiver caridade, não sou
nada". O principal nesta minha obra da Casa Verde é estudar profundamente a
loucura, os seus diversos graus, classificar-lhe os casos, descobrir enfim a causa do
fenômeno e o remédio universal. Este é o mistério do meu coração. Creio que com
isto presto um bom serviço à humanidade.
—Um excelente serviço, corrigiu o boticário.
—Sem este asilo, continuou o alienista, pouco poderia fazer; ele dá-me,
porém, muito maior campo aos meus estudos.
—Muito maior, acrescentou o outro.
E tinha razão. De todas as vilas e arraiais vizinhos afluíam loucos à Casa
Verde. Eram furiosos, eram mansos, eram monomaníacos, era toda a família dos
deserdados do espírito. Ao cabo de quatro meses, a Casa Verde era uma povoação.
Não bastaram os primeiros cubículos; mandou-se anexar uma galeria de mais trinta e
sete. O Padre Lopes confessou que não imaginara a existência de tantos doidos no
mundo, e menos ainda o inexplicável de alguns casos. Um, por exemplo, um rapaz
bronco e vilão, que todos os dias, depois do almoço, fazia regularmente um discurso
acadêmico, ornado de tropos, de antíteses, de apóstrofes, com seus recamos de grego
e latim, e suas borlas de Cícero, Apuleio e Tertuliano. O vigário não queria acabar de
crer. Quê! um rapaz que ele vira, três meses antes, jogando peteca na rua!
—Não digo que não, respondia-lhe o alienista; mas a verdade é o que Vossa
Reverendíssima está vendo. Isto é todos os dias.
— Quanto a mim, tornou o vigário, só se pode explicar pela confusão das
línguas na torre de Babel, segundo nos conta a Escritura; provavelmente, confundidas
antigamente as línguas, é fácil trocá-las agora, desde que a razão não trabalhe...
—Essa pode ser, com efeito, a explicação divina do fenômeno, concordou o
alienista, depois de refletir um instante, mas não é impossível que haja também
alguma razão humana, e puramente científica, e disso trato..."""

words = sentence.split()
bag_of_words = cp.deepcopy(words)
np.random.shuffle(bag_of_words)
# Bag of words:
print(bag_of_words)

# Annotated words:
# nltk.download('popular')
# Using natural language toolkit
print("Usando o natural language toolkit:")
# Use lang with ISO 639 code of the language
#pos_tags = nltk.pos_tag(sentence.split(), lang="pt") # not implemented.

# Reference to get the trained model:
# https://github.com/inoueMashuu/POS-tagger-portuguese-nltk
# trained_data_folder = 'data/'
portuguese_tagger = joblib.load('data/POS_tagger_brill.pkl')
pos_tags = portuguese_tagger.tag(nltk.word_tokenize(sentence))
print(pos_tags)
pos_tags_df = pd.DataFrame(pos_tags).T
print(pos_tags_df)

print("Usando o Spacy para se obter as partes do discurso.")
## https://spacy.io/models/pt
model_spacy = spacy.load('pt_core_news_sm')
pos_tags_2 = [ (word, word.pos_) for word in model_spacy(sentence)]
pos_tags_2_df = pd.DataFrame(pos_tags_2).T
print(pos_tags_2)
print(pos_tags_2_df)



