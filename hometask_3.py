variable_1 = input("Введіть перший продукт для покупки")
variable_2 = input("Введіть другий продукт для покупки")
variable_3 = input("Введіть третій продукт для покупки")
variable_4 = input("Введіть четвертий продукт для покупки")
variable_5 = input("Введіть п'ятий продукт для покупки")
list_buylist = [variable_1, variable_2, variable_3, variable_4, variable_5]
print(f'Твій поточний список покупок: {list_buylist}')
remove_1 = int(input("Введіть номер продукту, який ви вже купили"))
list_buylist.pop(remove_1 - 1)
print(f'Твій поточний список покупок: {list_buylist}')
remove_1 = int(input("Введіть номер продукту, який ви вже купили"))
list_buylist.pop(remove_1 - 1)
print(f'Твій поточний список покупок: {list_buylist}')
remove_1 = int(input("Введіть номер продукту, який ви вже купили"))
list_buylist.pop(remove_1 - 1)
print(f'Твій поточний список покупок: {list_buylist}')
remove_1 = int(input("Введіть номер продукту, який ви вже купили"))
list_buylist.pop(remove_1 - 1)
print(f'Твій поточний список покупок: {list_buylist}')
remove_1 = int(input("Введіть номер продукту, який ви вже купили"))
list_buylist.pop(remove_1 - 1)
if bool(list_buylist) is False:
    list_buylist.append(input("Додайте список покупок на наступний раз"))
    print(f'Ваш список покупок на наступний раз: {list_buylist}')
print("Дякуємо за користування нашими послугами. До побачення!")
