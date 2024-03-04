# EX 1 :categorisiti numerele de la 0 la 10 in pare si impare(folosind un for)

for i in range(0, 11):
    # print(f"Numarul curent este {i}")
    if i % 2 == 0:
        print(f'numarul {i} este par')
    # if i%2 != 0:
    else:
        print(f'numarul {i} este impar')
print("----" * 10)
# EX 2 CALCULATI SUMA NR IMPARE DE LA 1 LA 15
suma_impare = 0
for i in range(1, 16):
    if i % 2 != 0:
        suma_impare = suma_impare + i
print(f'suma numerelor impare este: {suma_impare}')
print("-----" * 10)

# EX3 - CALCULATI SUMA NR IMPARE DE LA 1 LA 15, FOLOSIND CUVANTUL CHEIE CONTINUE SI CONDITIA PUSA PE NUMERELE PARE(TEME)
suma_impare = 0
for i in range(0,16):
    if i % 2 != 0:
        continue 

# EX4 FACETI UN PROGRAM CARE SA NUMERE DE LA 10 IN JOS SI SA SARA PESTE NUMARUL 3 FOLOSIND WHILE
numar = 10
while numar <= 10 and numar >= 0:  # n!= 3 ,daca adaugam conditia aici programul se opreste la 4
    if numar != 3:
        print(numar)
    numar = numar - 1

#continuam acasa folosind continue
