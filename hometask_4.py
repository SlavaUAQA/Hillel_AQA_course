#task-1
list_variable_1 = input("Введіть вартість ваших покупок через пробіл").split()
sumelements = len(list_variable_1)
count = 0
for i in range(sumelements):
    count = (count + int(list_variable_1[i]))
count = count * 1.065
discount = input("Чи є у вас купон на знижку? (введіть так/ні)")
if discount == "ні":
    print(f'Сума вашої покупки складає {count}')
if discount == "так":
    discount_type = input("Ваша знижка на суму чи на відсоток? (введіть сума/відсоток)")
    if discount_type == "сума":
        amount = int(input("Введіть суму знижки"))
        print("Сума вашої покупки складає" + str(count - amount))
    if discount_type == "відсоток":
        percent = int(input("введіть відсоток знижки"))
        print("Сума вашої покупки складає" + str((count * ((100 - percent) / 100))))


#task-2
buylist = []
request = str(input("Введіть продукт, який ви хочете купити"))
buylist.append(request)
for request in range(100000):
    request = str(input("Введіть продукт, який ви хочете купити. Напишіть 'все' якщо більше не бажаєте вводити продукти "))
    buylist.append(request)
    if request == "все":
        break
buylist.pop()
print(f'Ваш поточний список покупок: {buylist}')
while buylist != []:
    products = int(input("Введіть номер продукту, який ви вже купили "))
    buylist.pop(products - 1)
    print(f'Ваш поточний список покупок: {buylist}')
if bool(buylist) is False:
    buylist.append(input("Додайте список покупок на наступний раз "))
    print(f'Ваш список покупок на наступний раз: {buylist}')
print("Дякуємо за користування нашими послугами. До побачення!")


#task-3

pincode = int(input("Введіть пінкод"))
amount = 0
while pincode != 7777:
    amount = amount + 1
    if amount == 3:
        print("Ви ввели невірний PIN CODE три рази. Вашу картку заблоковано")
        break
    print("Ви ввели невірний PIN CODE")
    pincode = int(input("Введіть PIN CODE"))

#task-4
name = "оЛенА"
age = 21
print(f'Я {name.title()}, мені {age} років')
print("Я {}, мені {} років".format(name.title(), age))
