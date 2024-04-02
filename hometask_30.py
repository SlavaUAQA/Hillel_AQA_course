# -*- coding: utf-8 -*-
import random

def generate_password(characters, length):
    chosen_characters = ''
    if '1' in characters:
        chosen_characters += 'abcdefghijklmnopqrstuvwxyz'
    if '2' in characters:
        chosen_characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if '3' in characters:
        chosen_characters += 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    if '4' in characters:
        chosen_characters += 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    if '5' in characters:
        chosen_characters += '0123456789'

    password = ''.join(random.choice(chosen_characters) for i in range(length))
    return password


characters = input(
    "Введіть символи, з яких має складатися пароль (1 - латинські маленькі літери, 2 - латинські великі літери, 3 - кирилиця маленькі літери, 4 - кирилиця великі літери, 5 - цифри): ")
length = int(input("Введіть довжину паролю: "))

password = generate_password(characters, length)
print("Ваш згенерований пароль:", password)
