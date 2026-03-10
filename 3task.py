#варіант 1

#введення року народження
birth_year_input = input("Введіть рік вашого народження: ")

#перевірка типу введенного числа (чи є цифрою)
if birth_year_input.isdigit():
    birth_year = int(birth_year_input) #рядок в число
    current_year = 2026 #поточний рік
    age = current_year - birth_year #обчислення віку
    print(f"Ваш вік: {age}") #вивід віку
else:
    print("Введене значення не є числом.") #повідомлення про помилку



