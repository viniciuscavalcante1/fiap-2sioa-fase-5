arquivo = open('fear.txt', encoding='UTF-8')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

arquivo = open('fear.txt', encoding='UTF-8')
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readlines())
print(arquivo.read())
arquivo.close()

# criar arquivos
conteudo = "Eu gosto de presentes"

arquivo = open("novo_arquivo.txt", "w", encoding='UTF-8')
arquivo.write(conteudo)
arquivo.close()