 # task-1
print("Додаткове завдання №1")
check_word = input(" Введіть слово для перевірки кількості литер")
print(f'Word "{check_word}" has ' + str(len(check_word)) + " letters")

#task-2
print("Додаткове завдання №2")
variable_1 = float(input(("ласкаво просимо до моєї першої програми калькулятора \nВведіть будь-ласка перше число")))
print(type(variable_1))
variable_2 = str(input("Введіть будь-ласка математичну дію, яку ви хочете виконати:\nВведіть 'додавання' для виконання додавання\nВведіть 'віднімання' для виконання віднімання\nВведіть 'множення' для виконання множення\nВведіть 'ділення' для виконання ділення\nВведіть 'степінь' для піднесення до степіня\nВведіть 'корінь' для зняття коріння\n"))
if variable_2 == "додавання" or variable_2 == "віднімання" or variable_2 == "множення" or variable_2 == "ділення":
    variable_3 = float(input(("Введіть будь ласка друге число ")))
    if variable_2 == "додавання":
        print(variable_1 + variable_3)
    elif variable_2 == "віднімання":
            print(variable_1 - variable_3)
    elif variable_2 == "множення":
        print(variable_1 * variable_3)
    elif variable_2 == "ділення":
        print(variable_1 / variable_3)
elif variable_2 == "степінь":
    variable_4 = float(input("введіть степінь в яку ви хочете возвести число"))
    print(variable_1 ** variable_4)
elif variable_2 == "корінь":
    variable_5 = float(input("введіть корінь якої степіні ви хочете зняти"))
    print(variable_1 ** variable_5)
