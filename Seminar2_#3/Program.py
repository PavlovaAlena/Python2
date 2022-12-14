#Задача 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

#************************
def lst_follow(n):
    return[round((1 + 1 / i)**i, 2) for i in range (1, n + 1)]   

#************************
import os 
os.system('cls')

print("Программа задает список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.")
n = int(input("Введите число n: "))

lst = lst_follow(n)

print(f"Список из {n} чисел последовательности {round((1+1/n)**n,2)}: {lst_follow(n)}")
print(f"Сумма чисел последовательности {round(sum(lst_follow(n)),2)}")