#guia rápido para instalar sem erros !!
import time
from os import system

def instalarDpendencias():
    print('primeiro instale as depencias:\n')
    system("echo ...")
    system("pip install setuptools")
    system("clear")
    system("apt-get install python2-dev libpcap0.8-dev libnetfilter-queue-dev libssl-dev libjpeg-dev libxml2-dev libxslt1-dev libcapstone-dev libffi-dev file")
    system("apt-get install python3-pip")
    system("pip3 install virtualenvwrapper")
    system("echo dependências instaladas !")
    system("clear")


def CriarVirtualEnv():
    print("qual o nome da pasta da que ira salvar o seu VirtualEnv:")
    pasta = input("")
    #criar pasta
    system(f"mkdir {pasta}")
    print(f'pasta {pasta} criada com sucesso !')
    system(f"cd {pasta}")
    print("qual o nome dar ao seu VirtualEnv:")
    nome = input("")
    print("criando...")
    system(f"virtualenv {nome} --python=python2")
    system(f"source {nome}/bin/activate")
    time.sleep(2)
    system("clear")
    print("está criado !")
    system("clear")


instalarDpendencias()
CriarVirtualEnv()

print('clonando directorio...')
system("git clone https://github.com/byt3bl33d3r/MITMf")
system("cd MITMf && git submodule init && git submodule update --recursive")
system("clear")
print('abrindo o mitmf :\n')
system("clear")
system("cd MITMf")
system("ls")
system("python mitmf.py --help")

#tudo certo #

