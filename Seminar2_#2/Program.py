 #Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#************************
def composition(n):
    resultList = []
    result = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            result = result*j
        resultList.append(result)
        result = 1

    return resultList


#************************
import os 
os.system('cls')

print("Программа принимает на вход число N и выдает набор произведений чисел от 1 до N.")
digit = int(input("Введите число: "))

lst = composition(digit)

print(f"Набор произведений чисел от 1 до {digit}: {lst}")