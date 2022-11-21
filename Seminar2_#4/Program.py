 #Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
 #          Позиции хранятся в файле file.txt - в одной строке одно число.

#************************
def inputlst(n):
    resultList = []
    for i in range(-n, n):
        resultList.append(i)
    return resultList

#************************
def composition(lstf):
    result = 1
    lstposf = []        
    fl = open("d:/Мои документы/Алена/Обучение/8_2Python/Seminar2_#4/file.txt", "r")
    try:
        for str in fl:
            if str == "" or int(str) >= len(lstf):
                break
            result *= lstf[int(str)]
            lstposf.append(int(str))
    finally:
        fl.close()
    return result, lstposf

#************************
import os 
os.system('cls')

print("Программа задает список из N элементов, заполненных числами из промежутка [-N, N].")
digit = int(input("Введите число N: "))

lst = inputlst(digit)
res, lstpos  = composition(lst)

print(f"Список из промежутка [-{digit}, {digit}]: {lst}")
print(f"Ппроизведение элементов на позициях {lstpos} равно {res}")