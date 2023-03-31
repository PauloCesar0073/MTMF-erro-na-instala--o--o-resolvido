#guia rápido para instalar sem erros !!
import time

import bash as bash
import os

def instalarDpendencias():
    print('primeiro instale as depencias:\n')
    bash.bash("")
    bash.bash("pip install setuptools")
    bash.bash("clear")
    bash.bash("apt-get install python2-dev libpcap0.8-dev libnetfilter-queue-dev libssl-dev libjpeg-dev libxml2-dev libxslt1-dev libcapstone-dev libffi-dev file")
    bash.bash("apt-get install python3-pip")
    bash.bash("pip3 install virtualenvwrapper")
    bash.bash("echo dependências instaladas !")
    bash.bash("clear")


def CriarVirtualEnv():
    print("qual o nome da pasta da que ira salvar o seu VirtualEnv:")
    pasta = input("")
    #criar pasta
    bash.bash(f"mkdir {pasta}")
    print(f'pasta {pasta} criada com sucesso !')
    bash.bash(f"cd {pasta}")
    print("qual o nome dar ao seu VirtualEnv:")
    nome = input("")
    print("criando...")
    bash.bash(f"virtualenv {nome} --python=python2")
    bash.bash(f"source {nome}/bin/activate")
    time.sleep(2)
    bash.bash("clear")
    print("está criado !")
    bash.bash("clear")


instalarDpendencias()
CriarVirtualEnv()

print('clonando directorio...')
bash.bash("git clone https://github.com/byt3bl33d3r/MITMf")
bash.bash("cd MITMf && git submodule init && git submodule update --recursive")
bash.bash("clear")
bash.bash("python mitmf.py --help")


