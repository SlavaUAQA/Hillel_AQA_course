#task-1: calculator
#Напишіть калькулятор, який запитує два числа якщо це множення, додавання, ділення, віднімання. Виводить на екран результат.
print("Завдання №1")
def foo_1(variable_1, variable_2):
    return variable_1 + variable_2
def foo_2(variable_1, variable_2):
    return variable_1 - variable_2
def foo_3(variable_1, variable_2):
    return variable_1 * variable_2
def foo_4(variable_1, variable_2):
    return variable_1 / variable_2

variable_1 = int(input("Ласкаво просимо до моєї першої програми калькулятора \nВведіть число №1 "))
math_action = input("Введіть будь-ласка математичну дію, яку ви хочете виконати:\nВведіть '+' для виконання додавання\nВведіть '-' для виконання віднімання\nВведіть '*' для виконання множення\nВведіть '/' для виконання ділення\n")
variable_2 = int(input("Введіть число №2 "))
if math_action == '+':
    print('Результат математичної діі між двома введеними числами буде:' + str(foo_1(variable_1, variable_2)))
elif math_action == '-':
    print('Результат математичної діі між двома введеними числами буде:' + str(foo_2(variable_1, variable_2)))
elif math_action == '*':
    print('Результат математичної діі між двома введеними числами буде:' + str(foo_3(variable_1, variable_2)))
elif math_action == '/':
    print('Результат математичної діі між двома введеними числами буде:' + str(foo_4(variable_1, variable_2)))
print()

#task-2: math actions
#Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).
# Так як робили на уроці. Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
#
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.


# Саме завдання звідси. Зробив інакше за допомогою функції. Трохи ускладнив завдання і додав регульований діапазон.
# Не зовсів розумію що за None вилітає в кінці кожної таблиці
print("Завдання №2")

def sum(i,j):
    result = range(i,j+1)
    for i in result:
        for j in result:
            print(f"{i}+{j}={i+j}", end=" \n",)
def sub(i,j):
    result = range(i, j+1)
    for i in result:
        for j in result:
            print(f"{i}-{j}={i-j}", end=" \n",)
def mult(i,j):
    result = range(i, j+1)
    for i in result:
        for j in result:
            print(f"{i}*{j}={i*j}", end=" \n",)
def div(i,j):
    result = range(i, j+1)
    for i in result:
        for j in result:
            print(f"{i}*{j}={i*j}", end=" \n",)
user_request = input("Введіть математичну дію, яку ви хочете надрукувати ('+', '-', '*' чи '/'):")
i = int(input("Введіть першу цифру діапазону математичної діі"))
j = int(input("Введіть другу цифру діапазону математичної дії"))
if user_request == '+':
    print(sum(i,j))
elif user_request == '-':
    print(sub(i,j))
elif user_request == '*':
    print(mult(i,j))
elif user_request == '/':
    print(div(i,j))
print()
