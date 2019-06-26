import eel
from cryptography.fernet import Fernet
from gdrive import upGdrive

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
        file_to_upload = arquivo + '.crypto'
    
    #teste de upload
    drive = upGdrive.autenticator()
    upGdrive.upload(file_to_upload, drive)

@eel.expose
def decrypt(arquivo):
    key = open_key()
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


eel.init('web')
eel.start('index.html', block=False)

while True:
    eel.sleep(10)
