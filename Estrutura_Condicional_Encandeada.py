sexo = input("Digite seu sexo [M | F ]:")
altura = float(input("Digite sua altura: "))

if sexo.upper() == "F":
    peso = (72.7 * altura) - 58
    print("Seu peso ideal é {:.2f}".format (peso))
elif sexo.upper() == "M":
    peso = (62.1 * altura) - 44.7
    print ("Seu peso ideal é {:.2f}".format (peso))
else:
    print("Opção de sexo inválida!")

    
