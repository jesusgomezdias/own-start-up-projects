mport random

num = []
r = [random.randint(0, 9)]

while len(num) < 6:
         numero = random.randint(1, 49)

         if not numero in numeros:
         num.append(numero)

print("numeros: ", num)
print("reintegro: ", r)
