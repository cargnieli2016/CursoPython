print("COVID-19")
suspeitos = 0
numero_pacientes = int(input("Informe a quantidade de pacientes: "))
cont = 1
while cont <= numero_pacientes:
    tosse = int(input("Tosse? \n1. Sim \n2. Não \nResp.: "))
    febre = int(input("Febre? \n1. Sim \n2. Não \nResp.: "))
    resp = int(input("Dificuldade de respirar? \n1. Sim \n2. Não \nResp.: "))

    if tosse == 1 and febre == 1 and resp == 1:
        suspeitos += 1

    cont += 1

print("Suspeitos de COVID-19: {}".format(suspeitos))
