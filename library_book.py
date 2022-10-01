import os

class Action:
    EXIT = 0
    ADD = 1
    LIST = 2
    DEL = 3
    BOOK = 4

class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.title}, {self.year}, {self.author}'


class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def removeAt(self, b):
        self.books.pop(b - 1)

    def printAll(self):
        for ind, book in enumerate(self.books, 1):
            st = str(book).split(',')
            print(ind, f'{st[0]}')

    def printAt(self, b):
        print(self.books[b - 1])


if __name__ == '__main__':
    libra = Library()
    book1 = Book('Темная башня', '1982', 'Стивен Кинг')
    book2 = Book('Анжелика', '1956', 'Анн и Серж Голон')
    book3 = Book('Идиот', '1868', 'Ф.М.Достоевский')
    libra.add(book1)
    libra.add(book2)
    libra.add(book3)
    select = None
    while select != '0':
        print(f'''
        Что будем делать?
        {Action.EXIT} - Выйти
        {Action.ADD} - Добавить книгу
        {Action.LIST} - Посмотреть список
        {Action.DEL} - Удалить книгу
        {Action.BOOK} - Информация о книге
        ''')
        select = input(">>: ")

        clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # Назначили ссылку на метод в поле clear
        clear()  # Вызываем при необходимости очистки консоли

        # exit
        if select == f'{Action.EXIT}':
            print('Пока.')
        # добавить
        elif select == f'{Action.ADD}':
            title = input('Введите название книги: ')
            year = input('Введите год издания книги: ')
            autor = input('Введите автора книги: ')
            book = Book(title, year, autor)
            libra.add(book)
        # список
        elif select == f'{Action.LIST}':
            libra.printAll()
        # удалить
        elif select == f'{Action.DEL}':
            b = int(input('Введите номер книги: '))
            libra.removeAt(b)
        # посмотреть инфо по номеру книги
        elif select == f'{Action.BOOK}':
            b = int(input('Введите номер книги: '))
            libra.printAt(b)
        # неправильный ввод
        else:
            print('\nНеправильный ввод!')
