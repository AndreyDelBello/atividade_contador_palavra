from collections import Counter
from unidecode import unidecode

with open('arquivo.txt', 'r') as arquivo_txt:
        texto = arquivo_txt.read()

# Função para carregar o arquivo e remover acentos
def carregar_arquivo(arquivo):
    with open(arquivo, 'r') as arquivo_txt:
        texto = arquivo_txt.read()
    return unidecode(texto)

# Função para realizar a contagem das palavras e exibir o ranking
def contar_palavras(texto):
    palavras = texto.lower().split()
    contador_palavras = Counter(palavras)
    ranking = contador_palavras.most_common()
    for palavra, frequencia in ranking:
        print(f'{palavra}: {frequencia}')
        
#print(contar_palavras(texto))

# Função para permitir que o usuário procure por palavras específicas
def procurar_palavras(texto):
    palavras = texto.lower().split()
    contador_palavras = Counter(palavras)
    palavras_procuradas = input('Digite as palavras que deseja procurar (separadas por vírgula): ').split(',')
    for palavra in palavras_procuradas:
        frequencia = contador_palavras.get(palavra.strip(), 0)
        print(f'A palavra "{palavra.strip()}" aparece {frequencia} vezes no arquivo.')
        
# Função para exibir a palavra mais e menos frequente
def exibir_extremos(texto):
    palavras = texto.lower().split()
    contador_palavras = Counter(palavras)
    palavra_mais_frequente = contador_palavras.most_common(1)[0][0]
    frequencia_mais_frequente = contador_palavras.most_common(1)[0][1]
    palavra_menos_frequente = contador_palavras.most_common()[-1][0]
    frequencia_menos_frequente = contador_palavras.most_common()[-1][1]
    print(f'A palavra com mais aparições é "{palavra_mais_frequente}" com {frequencia_mais_frequente} aparições.')
    print(f'A palavra com menos aparições é "{palavra_menos_frequente}" com {frequencia_menos_frequente} aparições.')
    
# Loop de menu principal
while True:
    print('\nMenu de opções:')
    print('1 - Carregar arquivo e retirar acentos')
    print('2 - Contar palavras e exibir ranking')
    print('3 - Procurar por palavras específicas')
    print('4 - Exibir palavra mais e menos frequente')
    print('0 - Encerrar aplicação')
    opcao = input('\nEscolha uma opção: ')
    
    if opcao == '1':
        arquivo = input('Digite o nome do arquivo: ')
        texto = carregar_arquivo(arquivo)
        print(f'Texto carregado:\n\n{texto}\n')
        
    elif opcao == '2':
        if not 'texto' in locals():
            print('É necessário carregar um arquivo antes de contar as palavras.')
        else:
            contar_palavras(texto)
            
    elif opcao == "3":
        print(procurar_palavras(texto))
       
    elif opcao == '4':
        arquivo = input('Digite o nome do arquivo: ')
        texto = carregar_arquivo(arquivo)
        if not 'texto' in locals():
            print('É necessário carregar um arquivo antes de exibir as palavras mais e menos frequentes.')
        else:
            exibir_extremos(texto)
            
    elif opcao == '0':
        print('Encerrando aplicação.')
        break
    else:
        print('Opção inválida. Tente novamente.')
