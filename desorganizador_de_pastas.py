import os

# muda a pasta de trabalho para o caminho especificado
os.chdir(r"c:\Users\fcris\Downloads")

# retorna somente o que for uma pasta no diretório atual
lista_pasta = [pasta for pasta in os.listdir() if os.path.isdir(pasta)]

for pasta in lista_pasta:
    lista_arquivos = os.listdir(pasta)
    for arquivo in lista_arquivos:
        pasta_destino = os.path.join(os.getcwd())
        de = os.path.join(os.getcwd(), pasta, arquivo)
        para = os.path.join(os.getcwd(), pasta_destino, arquivo)
        os.replace(de, para)

for pasta in lista_pasta:
    if not os.listdir(pasta):
        os.rmdir(pasta)

# esvazia a lixeira
os.system("PowerShell.exe -Command Clear-RecycleBin -Force")