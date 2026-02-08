

def open_spider_file():
    with open("spider.txt") as file:
        for line in file:
            print(line.strip().upper())


def write_files():
    with open("novel1.txt", "r+") as file:
        file.write("It was a dark and stormy night 3")

def ler_arquivo():
    dir = r"C:\scripts\_google-IT-Automation-with-Python\google-It-Automation-with-Python\programs\example_data_01.txt"
    with open(dir) as file:
        for line in file:
            print(line)


import os
import datetime

def criar_arquivo():
    """
    Cria um arquivo de texto temporário para testes de escrita
    """
    with open("teste01.txt", "w") as file:
        file.write("TESTE TESTE TESTE")

def apagar_arquivo():
    """
    Remove o arquivo 'teste01.txt' do diretório atual
    """
    os.remove("teste01.txt")

def renomear_arquivo():
    """
    Renomeia o arquivo 'teste01.txt' do diretório atual
    """
    os.rename("teste01.txt", "permanente01.txt")

def verificar_arquivo(name):
    """
    Verifica se um determinado arquivo existe no caminho
    """
    return os.path.exists(name) # True


def tamanho_arquivo(name):
    """
    Retorna o tamanho do arquivo
    """
    return os.path.getsize(name) # 217


def tempo_unix_arquivo(name):
    """
    Retorna o unix timestamp de um arquivo
    """
    return os.path.getmtime(name) # 1770501446.7214296


def tempo_arquivo(name):
    """
    Retorna data e tempo de um arquivo
    """
    timestamp = os.path.getmtime(name) 
    return datetime.datetime.fromtimestamp(timestamp) # 2026-02-07 18:57:26.721430


def caminho_arquivo(name):
    """
    Retorna o caminho completo de um arquivo
    """
    return os.path.abspath(name) # C:\scripts\_google-IT-Automation-with-Python\google-It-Automation-with-Python\programs\exemplo01.txt


def arquivo_arquivo(name):
    """
    Retorna se o arquivo existe
    """
    return os.path.isfile(name)


def diretorio_atual():
    """
    Retorna diretório atual
    """
    return os.getcwd() # C:\scripts\_google-IT-Automation-with-Python\google-It-Automation-with-Python\programs


def criar_diretorio():
    """
    Cria um diretório novo
    """
    os.mkdir("novo diretorio") # None


def mudar_diretorio():
    """
    Muda o diretorio
    """
    os.chdir("novo diretorio")
    return os.getcwd() # C:\scripts\_google-IT-Automation-with-Python\google-It-Automation-with-Python\programs\novo diretorio


def remover_diretorio():
    """
    Remove um diretorio
    """
    os.mkdir("newer dir")
    os.rmdir("newer dir")


def listar_diretorio():
    """
    Lista arquivos de um diretorio
    """
    return os.listdir() # ['.env', 'exemplo01.txt', 'novel1.txt', 'novo diretorio', 'spider.txt', 'using-python.py']


def funcao_website():
    dir = "website"
    for name in os.listdir(dir):
        fullname = os.path.join(dir, name)
        if os.path.isdir(fullname):
            print("{} is a directory".format(fullname))
        else:
            print("{} is a file".format(fullname))


if __name__ == "__main__":
    exemplo = "exemplo01.txt"
    # open_spider_file()
    # rite_files() 
    # ler_arquivo()
    # criar_arquivo()
    #apagar_arquivo()
    # renomear_arquivo()
    # verificar_arquivo("teste01.txt")
    # verificar_arquivo("permanente01.txt")
    # print(verificar_arquivo(exemplo))
    # print(tamanho_arquivo(exemplo))
    # print(tempo_unix_arquivo(exemplo))
    # print(tempo_arquivo(exemplo))
    # print(caminho_arquivo(exemplo))
    # print(arquivo_arquivo(exemplo))
    # print(diretorio_atual())
    # print(criar_diretorio())
    # print(mudar_diretorio())
    # remover_diretorio()
    # print(listar_diretorio())
    funcao_website()