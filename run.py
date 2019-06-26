import eel
from cryptography.fernet import Fernet

def key_generator():
    key = Fernet.generate_key()

    file = open('key.key', 'wb')
    file.write(key)
    file.close()

def open_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    #print(key)
    return(key)


@eel.expose
def crypto(arquivo):
    key = open_key()
    with open (arquivo, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(arquivo + '.crypto', 'wb') as file_enc:
        file_enc.write(encrypted)

def decrypto(arquivo, key):
    with open (arquivo, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    arquivo = arquivo.replace('.crypto', '')
    with open(arquivo, 'wb') as f:
        f.write(encrypted)

@eel.expose
def print_path(data):
    print(data)



'''arquivo = 'D:\Imagens\surfacefamily.jpg'
key = open_key()
crypto(arquivo)
#decrypto(arquivo, key)'''


eel.init('web')
eel.start('index.html', block=False)

while True:
    eel.sleep(10)
