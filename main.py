import random
import math
import copy

hints = True
menu = "\n1)Шифр простой одинарной перестановки\n2)Шифр блочной одинарной перестановки\n3)Шифр табличной маршрутной перестановки\n4)Шифр вертикальной перестановки\n5)Шифр 'Поворотная решетка'\n6)Шифр магический квадрат\n7)Шифр двойной перестановки\n8)Поменять текст\n9)Включить/Выключить подсказки\n"

def permutation(n):
    d = dict()
    used = []
    arr = []
    for i in range(n):
        ch = random.randint(0, n-1)
        while ch in used:
            ch = random.randint(0, n-1)
        used.append(ch)
        arr.append(ch+1)
        d[ch] = i
    if hints:
        print(list(range(1, n+1)))
        print(arr)
    return d

# Шифр простой одинарной перестановки
def permutationOne():
    print("Шифр простой одинарной перестановки")
    print("Исходний текст: " + text)
    cipher = ""
    d = permutation(len(text))
    for i in range(len(text)):
        cipher += text[d[i]]
    print("Результат: " + cipher)

# Шифр блочной одинарной перестановки
def permutationBlock():
    print("Шифр блочной одинарной перестановки")
    print("Исходний текст: " + text)
    Step = int(input("Введите длину блока: ")) 
    t = text
    cipher = ""
    d = permutation(Step)
    if len(text) % Step != 0:
        for i in range(Step - len(text) % Step):
            t += chr(random.randint(ord("a"), ord("z")))
        if hints:
            print("После дописывания: " + t)
    for i in range(0, len(t), Step):
        for j in range(Step):
            cipher += t[i + d[j]]
    print("Результат: " + cipher)

def printTable(arr):
    for i in range(len(arr)):
        print('[', end = "")
        for j in range(len(arr[i])):
            print(arr[i][j], end="")
            if j < len(arr[i])-1:
                print(", ", end="")
        print(']')

def table(M, N):
    i = 0
    arr = []
    for m in range(M):
        a = []
        for n in range(N):
            if i < len(text):
                a.append(text[i])
            else:
                a.append('_')
            i += 1
        arr.append(a)
    if hints:
        printTable(arr)
    return arr

# Шифр табличной маршрутной перестановки
def routeTable():
    print("Шифр табличной маршрутной перестановки")
    print("Исходний текст: " + text)
    N = int(input("Введите длину таблицы: "))
    M = int(input("Введите высоту таблицы: "))
    while M*N < len(text):
        print("Размер таблицы меньше длины текста")
        N = int(input("Введите длину таблицы: "))
        M = int(input("Введите высоту таблицы: "))
    cipher = ""
    arr = table(M, N)
    for n in range(N):
        for m in range(M):
            cipher += arr[m][n]
    print("Результат: " + cipher)

# Шифр вертикальной перестановки
def permutationVertical():
    print("Шифр вертикальной перестановки")
    print("Исходний текст: " + text)
    Step = input("Введите лозунг: ")
    d = dict()
    cipher = ""
    arrABC = []
    arr = [[], []]
    for i in Step:
        arrABC.append(i)
    arrABC.sort()
    for i in range(len(Step)):
        arr[0].append(Step[i])
        j = arrABC.index(Step[i])
        arr[1].append(j)
        d[j] = i
        arrABC[j] = '  '
    if hints:
        printTable(arr)
        print('Запись таблицы')
    arrTable = table(math.ceil(len(text) / len(Step)), len(Step))
    for i in range(len(arr[1])):
        for j in range(len(arrTable)):
            cipher += arrTable[j][d[i]]
    print("Результат: " + cipher)

def printTableBool(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]:
                print('+', end=' ')
            else:
                print('-', end=' ')
        print()

def inTable(arr1, arr2, s):
    if hints:
        printTableBool(arr2)
    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            if arr2[i][j]:
                if s < len(text):
                    arr1[i][j] = text[s]
                else:
                    arr1[i][j] = '_'
                s += 1
    if hints:
        printTable(arr1)
        print()
    return arr1

# Шифр 'Поворотная решетка'
def rotateTable():
    print("Шифр 'Поворотная решетка'")
    print("Исходний текст: " + text)
    k = int(input("Введите длину/высоту таблицы: "))
    while k % 2 != 0:
        print('Число должно быть чётным')
        k = int(input("Введите длину/высоту таблицы: "))
    cipher = ""

    arr = []
    for i in range(k):
        a = []
        for j in range(k):
            a.append(False)
        arr.append(a)
    arr1 = copy.deepcopy(arr)
    arr2 = copy.deepcopy(arr)
    arr3 = copy.deepcopy(arr)
    arr4 = copy.deepcopy(arr)

    kk = k*k >> 2
    for i in range(kk):
        x = random.randint(0, k-1)
        y = random.randint(0, k-1)
        while arr[x][y]:
            x = random.randint(0, k-1)
            y = random.randint(0, k-1)
        arr1[x][y] = True
        arr2[k-x-1][y] = True
        arr3[x][k-y-1] = True
        arr4[k-x-1][k-y-1] = True

        arr[x][y] = True
        arr[x][k-y-1] = True
        arr[k-x-1][y] = True
        arr[k-x-1][k-y-1] = True

    arrTable = []
    for i in range(k):
        a = []
        for j in range(k):
            a.append(' ')
        arrTable.append(a)

    arrTable = inTable(arrTable, arr1, 0)
    arrTable = inTable(arrTable, arr3, kk)
    arrTable = inTable(arrTable, arr4, kk*2)
    arrTable = inTable(arrTable, arr2, kk*3)
    for i in range(4):
        for j in range(4):
            cipher += arrTable[j][i]
    print("Результат: " + cipher)

def addText():
    t = text
    if len(text) > 16:
        print('решётка 4х4 не может вместить весть шифр')
    elif len(text) < 16:
        for i in range(16 - len(text)):
            t += '.'
    return t

# Шифр магический квадрат
def magic4x4():
    print("Шифр магический квадрат")
    print("Исходний текст: " + text)
    cipher = ""
    t = addText()
    arr = [[ t[15], t[2],  t[1],  t[12]],
            [t[4],  t[9],  t[10], t[7]],
            [t[8],  t[5],  t[6],  t[11]],
            [t[3],  t[14], t[13], t[0]]]
    if hints:
        printTable(arr)
    for i in range(4):
        for j in range(4):
            cipher += arr[i][j]
    print("Результат: " + cipher)

# Шифр двойной перестановки
def permutationTable():
    print("Шифр двойной перестановки")
    print("Исходний текст: " + text)
    cipher = ""
    N = int(input("Введите длину таблицы: "))
    M = int(input("Введите высоту таблицы: "))
    while M*N < len(text):
        print("Размер таблицы меньше длины текста")
        N = int(input("Введите длину таблицы: "))
        M = int(input("Введите высоту таблицы: "))
    arrTable = table(M, N)
    if hints:
        print("Перемешивание столбцов")
    d = permutation(N)
    arr1 = []
    for i in range(M):
        a = []
        for j in range(N):
            a.append(arrTable[i][d[j]])
        arr1.append(a)
    if hints:
        print("Таблица после перемешивания столбцов")
        printTable(arr1)
        print("Перемешивание строк")
    d = permutation(M)
    arr2 = []
    for i in range(M):
        a = []
        for j in range(N):
            a.append(arr1[d[i]][j])
        arr2.append(a)
    if hints:
        print("Таблица после перемешивания строк")
        printTable(arr2)
    for i in range(N):
        for j in range(M):
            cipher += arr2[j][i]
    print("Результат: " + cipher)

text = input("Введите текст: ")
while True:
    print(menu)
    step = input("Выберите номер действия: ")
    if step in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        step = int(step)
        if step == 8:
            text = input("Введите текст: ")
        elif step == 9:
            hints = not hints
        elif step == 1: permutationOne()
        elif step == 2: permutationBlock()
        elif step == 3: routeTable()
        elif step == 4: permutationVertical()
        elif step == 5: rotateTable()
        elif step == 6: magic4x4()
        elif step == 7: permutationTable()
    else:
        print("Неверный ввод")