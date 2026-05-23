'''
Create a directory and move a file from one directory to another using low-level os functions
'''

import os


def os_principal():
    # Check to see if a directory named "test1" exists under the current directory. If not, create it:
    dest_dir = os.path.join(os.getcwd(), "test1")
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
        
    # Construct source and destination paths:
    src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
    dest_file = os.path.join(os.getcwd(), "test1", "README.md")

    # Move the file from its original location to the destination:
    os.rename(src_file, dest_file)
    return





# Funções OS

def os_path_abspath():
    '''
    os.path.abspath(path)
    '''
        
    print(" --- ")
    print("def os_path_abspath():")
    print(" --- ")
    
    caminho_relativo = 'novel.txt'
    caminho_absoluto = os.path.abspath(caminho_relativo)

    print("Relativo: ", caminho_relativo)
    print("Absoluto: ", caminho_absoluto)
    return

def os_path_join():
    '''
    os.path.join(path, /, *paths)
    Join one or more path segments intelligently.
    '''
        
    print(" --- ")
    print("os.path.join(path, /, *paths)")
    print(" --- ")
    
    pasta_base = 'meus_documentos'
    nome_arquivo = 'relatorio_mensal.txt'

    caminho_final = os.path.join(pasta_base, nome_arquivo)
    print(caminho_final)
    return

def os_path_exists():
    '''
    os.path.exists(path)
    '''
        
    print(" --- ")
    print("os.path.exists(path)")
    print(" --- ")
    
    caminho_existe = r'C:\scripts\_google-IT-Automation-with-Python\google-It-Automation-with-Python\02_Using-Python-to-Interact-with-the-Operating-System\module02\existe.txt'
    
    if os.path.exists(caminho_existe):
        print("O arquivo foi encontrado!")
    else:
        print("Ops, o arquivo ou a pasta não existe. Verifique o endereço.")
        
    
    caminho_nao_existe = r'C:\scripts\_google-IT-Automation-with-Python\google-It-Automation-with-Python\02_Using-Python-to-Interact-with-the-Operating-System\module02\nao_existe.txt'
    
    if os.path.exists(caminho_nao_existe):
        print("O arquivo foi encontrado!")
    else:
        print("Ops, o arquivo ou a pasta não existe. Verifique o endereço.") 
    return

def os_getcwd():
    '''
    os.getcwd()
    Return a string representing the current working directory.
    '''
        
    print(" --- ")
    print("os.getcwd()")
    print(" --- ")
    
    # Pega o diretório atual
    pasta_atual = os.getcwd()
    
    print(f"O meu terminal está rodando a partir desta pasta: {pasta_atual}")
    return

def os_rename():
    '''
    os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
    Rename the file or directory src to dst.
    '''
        
    print(" --- ")
    print("os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)")
    print(" --- ")
    
    # Nome atual (src) e o novo nome que queremos dar (dest)
    nome_antigo = "novel.txt"
    nome_novo = "romance_finalizado.txt"
    
    # Executando o renomeio
    os.rename(nome_antigo, nome_novo)
    
    print(f"Sucesso! O arquivo '{nome_antigo}' agora se chama '{nome_novo}'")
    return

if __name__ == '__main__':
    os_principal()
    # os_path_abspath()
    # os_path_join()
    # os_path_exists()
    # os_getcwd()
    # os_rename()