
valor_PI = 3.14

def saudar():
    print("Olá")

def saudar_aluno(nome):
    print("Olá, {}".format (nome))

def calcula_dobro(numero):
    return 2 * numero

def calcula_dobro_triplo(numero):
    return 2 * numero, 3 * numero

def calcula_area_circulo():
    raio = 3
    return valor_PI * pow(raio, 2)

def calcula_comprimento_circulo():
    return 2 * valor_PI * raio
