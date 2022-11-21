#Задача 5. Реализуйте алгоритм перемешивания списка.

#************************
def lst_mixed(lstOr):
    lstM = lstOr[:]
    import random
    for i in range(len(lstOr)):
        index_ran = random.randint(0, len(lstOr) - 1)
        temp = lstM[i]
        lstM[i] = lstM[index_ran]
        lstM[index_ran] = temp
    return lstM

#************************
def inputlst(N):
    lst = []
    for x in range(N):
        x = input(f"Введите данные для {x+1} элемента списка: ")
        try: lst.append(int(x))
        except ValueError: lst.append(x)
    return lst    

#************************
import os 
os.system('cls')

print("Программа реализует алгоритм перемешивания списка. В данном случае - в случайном порядке")

N = int(input("Введите размер списка: "))
lst = inputlst(N)

lstMix = lst_mixed(lst)

print(f"Список исходный {lst}")
print(f"Список перемешанный {lstMix}")