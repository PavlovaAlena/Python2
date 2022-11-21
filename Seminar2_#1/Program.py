# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#************************
def sum_digit(dig):
    result = 0
    numCalc = abs(dig)
    for i in str(numCalc):
        if i != '.':
            result += int(i)
    return result

#************************
import os 
os.system('cls')

print("Программа принимает на вход вещественное число и показывает сумму его цифр.")
digit = float(input("Введите число: "))

sum = sum_digit(digit)

print(f"В числе {digit} сумма цифр = {sum}")

# Второй вариант решения (если целое число)
""" def sum_digit(dig):

    result = 0
    numCalc = abs(dig)
    while (numCalc // 10 != 0):
    
        result = result + numCalc % 10
        numCalc = numCalc // 10
   
    result = result + numCalc
    return int(result) """