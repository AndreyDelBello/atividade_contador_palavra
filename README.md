# atividade_contador_palavra

Primeiramente eu abri o arquivo txt com o python.
Em seguida criei funçoes para cada atividade solicitada.

Então na primeira função ele carrega o arquivo recebe o nome do arquivo que será carregado como parâmetro e retorna o texto contido no arquivo, sem acentos, utilizando a função unidecode da biblioteca unidecode. Na última linha, o texto é carregado a partir do arquivo arquivo.txt.

Nesta linha, a função unidecode é utilizada para remover os acentos do texto carregado anteriormente.
texto_sem_acentos = unidecode(texto)

A função contar_palavras recebe o texto sem acentos como parâmetro e retorna um dicionário contendo as palavras e o número de vezes que cada uma delas aparece no texto.
O processo de contagem é feito utilizando o método split() para dividir o texto em palavras, e um loop for para iterar sobre cada palavra e atualizar o dicionário contagem de acordo com o número de vezes que a palavra aparece.
Ao final deste processo, a variável contagem_palavras contém o dicionário com as palavras e o número de vezes que cada uma delas aparece no texto.

A opção de permitir ao usuário saber quais palavras e quantas vezes elas aparecem foi feita:
Primeiro, o programa solicita ao usuário que digite a palavra que deseja buscar. Em seguida, o programa verifica se a palavra está presente no dicionário contagem_palavras. Se a palavra estiver presente, o programa exibe o número de vezes que a palavra aparece no texto. Caso contrário, o programa exibe uma mensagem informando que a palavra não foi encontrada no texto.
