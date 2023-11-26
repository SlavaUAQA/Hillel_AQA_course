#TODO: 1. Написати програму, яка буде зчитувати з консолі число.
# dict_actions = {"+":range(2, 10), "-":range(2, 10), "*":range(2, 10), "/":range(2, 10)}
# user_request = input("Введіть математичну дію, яку ви хочете надрукувати ('+', '-', '*' чи '/'):")
# if user_request == "+":
#     for i in dict_actions["+"]:
#         for j in dict_actions["+"]:
#             print(f"{i}+{j}={i+j}", end=" \n",)
# elif user_request == "-":
#     for i in dict_actions["-"]:
#         for j in dict_actions["-"]:
#             print(f"{i}-{j}={i-j}", end=" \n")
# elif user_request == "*":
#     for i in dict_actions["*"]:
#         for j in dict_actions["*"]:
#             print(f"{i}*{j}={i*j}", end=" \n")
# elif user_request == "/":
#     for i in dict_actions["/"]:
#         for j in dict_actions["/"]:
#             print(f"{i}/{j}={i/j}", end=" \n")
# print()

dict_actions = {"+": range(2, 10), "-": range(2, 10), "*": range(2, 10), "/": range(2, 10)}
user_request = input("Введіть математичну дію, яку ви хочете надрукувати ('+', '-', '*' чи '/'):")
if user_request in dict_actions:
    for i in dict_actions[user_request]:
        for j in dict_actions[user_request]:
            result = f"{i}{user_request}{j}"
            print(f"{i}{user_request}{j} = {eval(result)}")
print()
