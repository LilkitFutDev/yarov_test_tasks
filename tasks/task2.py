import os

input = input("Введите имя:")
name = "Вячеслав"
if input == name :
    print("Привет,{0}".format(name))
else:
    print("Нет такого имени")

os.system('pause')