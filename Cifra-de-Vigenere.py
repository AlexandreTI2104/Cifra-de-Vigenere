import string
from collections import Counter

alfabeto = list (string.ascii_lowercase)

frequencia_letras_ingles = {'a' : 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966 , 'j' : 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n' : 6.749, 'o' : 7.507, 'p': 1.929, 'q': 0.095, 'r':5.987, 's': 6.327 , 't': 9.056 , 'u': 2.758, 'v': 0.978, 'w': 2.360,'x': 0.150, 'y': 1.974, 'z': 0.074}
frequencia_letras_portugues = {'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99, 'e': 12.57, 'f': 1.02, 'g': 1.30, 'h': 1.28, 'i': 6.18, 'j': 0.40, 'k': 0.02, 'l': 2.78, 'm': 4.74, 'n': 5.05, 'o': 10.73, 'p': 2.52, 'q': 1.20, 'r': 6.53, 's': 7.81, 't': 4.34, 'u': 4.63, 'v': 1.67, 'w': 0.01,
'x': 0.21, 'y': 0.01, 'z': 0.47}


# Criamos uma função onde vai cifrar a mensagem.
def cifracaodevigenere(message,senha):
  pos_chave = 0
  alfabeto_parcial = []
  resultado_cifra = ''
  for i in range (len(message)): 
    if message[i] == '.':
      resultado_cifra += '.'
    elif message[i] == ',':
      resultado_cifra += ','
    elif message[i] == ' ':
      resultado_cifra += ' ' 
    else:         
      num_posicao_caracter_texto = alfabeto.index(message[i]) #Procurei a posição de cada caracter do texto no alfabeto.
      # Para a posição da chave ir atualizando, criamos uma variável pos_chave = 0 e vai incrementando enquanto analisa. Se ela chegar ao tamanho da senha(len(senha)),  atualiza a posição da chave, se não, reseta pois tem que começar a senha do 0 para continuar comparando com a mensagem.
      if(pos_chave < (len(senha))): #Procurei a posição de cada caracter da senha no alfabeto
        num_posicao_caracter_senha = alfabeto.index(senha[pos_chave])
        pos_chave = pos_chave + 1
      else: # O else é resetado quando a mensagem é maior que a senha, por isso, abrange a posição da chave incrementando-a.
        pos_chave = 0
        num_posicao_caracter_senha = alfabeto.index(senha[pos_chave])
        pos_chave = pos_chave + 1 
        # Geração da tabela cíclica de cada linha do alfabeto conforme o vídeo, passado pelo professor fizemos apenas o complementar de dois arrays. 
      alfabeto_parcial = alfabeto[num_posicao_caracter_senha:] + alfabeto[0: num_posicao_caracter_senha]  
      cifra = alfabeto_parcial[num_posicao_caracter_texto] # Achando cada caracter da cifra correspondente ao texto a ser cifrado de acordo com o número da posição.
      resultado_cifra = resultado_cifra + cifra # Juntando as letras formando o resultado dessa cifra.
  return resultado_cifra


# Criamos uma função onde vai decifrar a mensagem.
def decifracaodevigenere(messagecifrada,senha):
  pos_senha = 0
  alfabeto_parcial = []
  resultado_decifrado = ''
  for i in range (len(messagecifrada)): 
    if messagecifrada[i] == '.':
      resultado_decifrado += '.'
    elif messagecifrada[i] == ',':
      resultado_decifrado += ','
    elif messagecifrada[i] == ' ':
      resultado_decifrado += ' ' 
    elif messagecifrada[i] == '-':
      resultado_decifrado += '-' 
    elif messagecifrada[i] == ';':
      resultado_decifrado += ';' 
    elif messagecifrada[i] == "'":
      resultado_decifrado += "'"
    else:
      num_posicao_caracter_senha = alfabeto.index(senha[pos_senha]) # Pega o indice da senha no alfabeto.
      alfabeto_parcial = alfabeto[num_posicao_caracter_senha:] + alfabeto[0: num_posicao_caracter_senha] # Geração da tabela ciclica de acordo com a senha.
      num_posicao_caracter_texto = alfabeto_parcial.index(messagecifrada[i]) # Pesquisando o indice de cada caracter da mensagem cifrado no alfabeto parcial.
      decifrado_caracter = alfabeto[num_posicao_caracter_texto] # Achando cada caracter do texto decifrado no alfabeto.
      resultado_decifrado = resultado_decifrado + decifrado_caracter  # Juntando as letras formando o resultado dessa decifração.
      if(pos_senha < (len(senha) - 1)): # -1 , pois a primeira letra foi pega na linha 52, e nesse caso vai seguir no restante das posições da senha.
        pos_senha = pos_senha + 1
      else: # É resetado a posição da senha
        pos_senha = 0
  return resultado_decifrado


# Criamos uma função para pontuar as frequências em português e inglês.
def diferencia(messagecifrada, frequencia):
  b = [] # Criando uma lista para adicionar cada letra do alfabeto que vai passar pelo "a".
  contador = Counter(messagecifrada) # Montando as ocorrências das letras da mensagem cifrada
  for letras in alfabeto: # Procurando as letras no alfabeto
    a = sum([abs(contador.get(letras, 0) * 100 / len(messagecifrada) - frequencia[letras])]) # Somando a porcentagem das letras de acordo com a messagem cifrada e retorna o valor absoluto do contador.
    #print(a)
    b.append(a) # Adicionando os elementos da lista.
    c = sum(map(float,b)) # Mapeando os números floats da lista e resume/soma os elementos da lista.
    d = c / 26 # Depois de adquirir a soma dos elementos na lista, podemos normalizar dividindo pelo tamanho do alfabeto português.
  return  d


def main():
  senha = str(input('Senha: ')).lower()
  message = str(input('Texto a ser cifrado: ')).lower()
  print('Texto Cifrado:', cifracaodevigenere(message, senha))
  
  senha = str(input('\nSenha: ')).lower()
  messagecifrada = str(input('Texto a ser decifrado: ')).lower()
  print('Texto Decifrado:', decifracaodevigenere(messagecifrada, senha))
  
  input("Pressione Enter para fechar.") # Trava a tela do usuário.

main()
