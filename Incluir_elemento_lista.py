nomes = []

while True:
    nome = input("Digite um nome de uma pessoa: ")
    nomes.append(nome)

    resp = input("Deseja continuar [S|N] ")
    if resp.upper() == "N":
        break

for index in nomes:
    print(index)
