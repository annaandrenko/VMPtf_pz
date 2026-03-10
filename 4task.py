#варіант 1

class Book:
    def __init__(self, title, author, year): #конструктор для задання характеристик
        self.title = title #назва
        self.author = author #автор
        self.year = year #рік видання

    def display_info(self): #метод для виводу характеристик
        print("Назва книги:", self.title)
        print("Автор:", self.author)
        print("Рік видання:", self.year)

#створення обєкту класу
my_book = Book("Head First Python", "Пол Беррі", 2021)

#виклик методу виводу характеристик
my_book.display_info()