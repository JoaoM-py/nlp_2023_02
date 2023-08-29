# EXERCÍCIOS DE PROCESSAMENTO DE LINGUAGEM NATURAL

TC.1.1. Selecione uma obra literária de domínio público (ex. livros tais como Vinte mil léguas
submarinas (de Júlio Verne), a Bíblia, etc.) e ilustre a variedade de dados presente. Considere,
por exemplo a construção de frases, orações etc. e compare com expressões de uso corrente

Ia a entrar na sala de visitas, quando ouvi proferir o meu nome
e escondi-me atrás da porta.

Este dado contém a estrutura de uma frase formal geralmente falada em ambientes mais sérios

ex: “"Estava prestes a entrar na sala quando ouvi alguém chamando meu nome e me escondi rapidamente.””

Não acho. Metidos nos cantos?

Você o que quer é um capote;

As duas frases utilizam estruturas de assimilação onde geralmente são entendidas pelas pessoas que utilizam essas gírias. Mantem o contexto da região e da época

ex:  “**Tô na correria**”, “**Não tô nem aí”**

TC.1.2. Exemplifique uma sentença, escrita na língua portuguesa, que pode surgir em um site de
pré-atendimento em uma concessionária, que potencialmente seja diİcil de ser interpretado por
um chatbot. Explique sua resposta em termos de estruturação da sentença e suponha que ela
esteja gramaƟcalmente correta.

Gostaria de solicitar um reparo no meu carro pois a janela foi quebrada e meu mecanico disse
isso pode interferir no funcionamento do parabriza e isso pode ser um problema ja que vou precisar trocar as pastilhas, vocês teriam esse tipo de serviço?

TC. 1.3. Sistemas de PNL são geralmente compostos por modelos que são treinados utilizando
corpora de texto. Por que modelos que são válidos hoje podem não mais ser adequados daqui a
dois anos?

Corpora cria contextos baseados no que estamos vivendo/passando, os contextos mudam a partir dos anos

TC.1.4. Por que a utilização de emojis ou outros símbolos não presentes na linguagem textual
formal podem dificultar a operação de um sistema de PNL?

Não há como fazer análises semânticas e estruturais com emojis, logo torna-se impossível de se criar um contexto só com elas.

TC.1.5. Dê um exemplo de sentença em um processo comunicativo onde a os referentes
considerados pelo transmissor e pelo receptor podem ser distintos caso não haja adequada
contextualização do processo comunicativo.

Ele disse para ela que estava dentro do carro.

TC 1.6

**Lematização:**

análise morfológica das palavras 

- "amanheceu" -> "amanhecer"
- "estudantes" -> "estudante"
- "apressados" -> "apressado"
- "acordaram" -> "acordar"
- "saíram" -> "sair"
- "correndo" -> "correr"
- "fazer" -> "fazer"
- "a" -> "a" 
"Assim que amanhecer, o estudante, apressado, acordar e sair correndo para fazer o prova."

**Stemização:**

remove sufixos e prefixos, obtendo a raiz.

- "amanheceu" -> "amanhec"
- "estudantes" -> "estudant"
- "apressados" -> "apress"
- "acordaram" -> "acord"
- "saíram" -> "saír"
- "correndo" -> "corrend"
- "fazer" -> "faz"
- "a" -> "a" 
"Assim que amanhec, os estudant, apress, acord e saír corrend para faz a prova."

TC 1.7

Na pontuação, identificar se a frase é uma pergunta
Você está bem ?

- Você (PRON - Pronome)
- está (VERB - Verbo)
- bem (ADV - Advérbio)
- ? (PUNCT - Pontuação - Interrogação)

"Cats meow loudly."

identificar as categorias gramaticais

- Cats (NOUN - Substantivo)
- meow (VERB - Verbo)
- loudly (ADV - Advérbio)
