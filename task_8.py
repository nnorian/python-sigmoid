# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = []
for i in range(1, 11):
    numbers.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for num in numbers:
    if num % 2 == 0:
        print(num)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
    
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {'name': 'Snowden', 'age': 40, 'city': 'not known'}
for key, value in person.items():
    print(key, ":", value)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for sublist in matrix:
    for item in sublist:
        print(item)
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() 
# și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
for num in range(4, 11):
    print(num)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a 
# afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
list = ['what', 'am', 'i', 'doing']

for index, value in enumerate(list):
    print("Index:", index, "- Value:", value)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
list1 = ['hasta', 'la', 'vista', 'babe']
list2 = ['you', 'should', 'smile', 'more']
for item1, item2 in zip(list1, list2):
    print(item1, item2)
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = []
for i in range(1, 11):
    numbers.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei 
#până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
index = 0  
while index < len(numbers) and numbers[0] <= 50:  
    numbers[index] *= 2 
    index += 1 
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
perfect_squares = [num for num in range(1, 101) if int(num ** 0.5) ** 2 == num]
print(perfect_squares)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
number = 7
for i in range(1, 11):
    print(number, 'x', i, '=', number * i)
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
pairs_list = [[i, j] for i in range(1, 6) for j in range(1, 6)]
print(pairs_list)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for pair in pairs_list:
    if pair[0] < pair[1]:
        print(pair)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
numbers_random = [426, 8, 13, 5]

found = False
index = 0

while index < len(numbers_random):
    if numbers_random[index] > 10:
        print( numbers_random[index])
        found = True
        break
    index += 1

if not found:
    print("Nu există valori mai mari decât 10")
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
for i in range(5):
    for j in range(5):
        print("*", end='')
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(1, 7):
    for j in range(1, i+1):
        print(j, end='')
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(5, 0, -1):
    for j in range(5, 5-i, -1):
        print(j, end='')
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
for i in range(7):
    for j in range(i, 7):
        print(chr(97 + j), end='')
    print()
""" apparently learning char lists at school wasnt such a bad ideea
but i hope that at some point i wont start writing in binar code"""
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
for i in range(8):
    for j in range(16):
        if (i + j) % 2 == 0:
            print('+', end='')
        else:
            print('-', end='')
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
for i in range(2, 7):
    for j in range(1, i):
        print(3**j, end=" ")
    print()

for i in range(2, 6):
    for j in range(i, 6):
        print(3**j, end=" ")
    print()
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.