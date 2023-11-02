import io
#with io.open("meu_arquivo.txt", 'w') as arquivo:
#    arquivo.write("Ola mundo")

with io.open("meu_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)