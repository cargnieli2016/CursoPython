 import random
 while True:
     lin = int(input("Informe a quantidade de linhas da matriz: "))
     col = int(input("Informe a quantidade de colunas da matriz: "))
     if lin > 0 and col > 0:
         M = []
         for i in range(lin):
             LINHA = []
             for j in range(col):
                 num = random.randint(1, 16)
                 LINHA.append(num)
                M.append(LINHA)
            break
print(M)
        
              
