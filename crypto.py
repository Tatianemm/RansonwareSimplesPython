from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad #funções usadas para o padding

senha = b'FIAPfiap20232023' #128 bits = 16 caracteres
mensagem = b'Ola Mundo' # o "b" antes da senha e da mensagem indica que a variável deve ser tratada como bits

criptografia = AES.new(senha, AES.MODE_EAX) # salava o modo usado para encriptar
cifra, tag = criptografia.encrypt_and_digest(mensagem) #valor encriptado vai para cifra e o valor de digest vai para tag para validar a encriptação
nonce = criptografia.nonce #aumenta a aleatoriedade
print("Dado encriptado:", cifra)

des_criptografia = AES.new(senha, AES.MODE_EAX, nonce=nonce) # salava o modo usado para dsencriptar
decripta = des_criptografia.decrypt_and_verify(cifra, tag) #decripta a mensagem (cifra) verificando a tag
print("Dado desencriptado:", des_criptografia)

...

# Utilizando o PADDING


senha = b'FIAPfiap20232023' #128 bits = 16 caracteres
mensagem = b'Ola Mundo' # o "b" antes da senha e da mensagem indica que a variável deve ser tratada como bits

criptografia = AES.new(senha, AES.MODE_EAX) # salava o modo usado para encriptar
dado = pad(mensagem, AES.block_size) # indica a quantidade de bits que terá a chave 
cifra, tag = criptografia.encrypt_and_digest(mensagem) #valor encriptado vai para cifra e o valor de digest vai para tag para validar a encriptação
nonce = criptografia.nonce #aumenta a aleatoriedade
print("Dado encriptado:", cifra)

des_criptografia = AES.new(senha, AES.MODE_EAX, nonce=nonce) # salava o modo usado para dsencriptar
decripta = des_criptografia.decrypt_and_verify(cifra, tag) #decripta a mensagem (cifra) verificando a tag
clean = unpad(decropta, AES.block_size)  #retira o pad para que a mensagem esteja do tamanho correto
print("Dado desencriptado:", des_criptografia)



