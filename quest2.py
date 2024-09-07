string = input("Digite uma string: ")

existe_a = False
quantidade_a = 0

for letra in string:
    if letra.lower() == 'a':
        existe_a = True
        quantidade_a += 1

if existe_a:
  print(f"A letra 'a' existe no texto e ocorre {quantidade_a} vezes.")
else:
  print("A letra 'a' não existe no texto.")