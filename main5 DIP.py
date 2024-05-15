# Принцип инверсии зависимости (DIP, Dependency Inversion Principle)

class Book():
    def read(self):
        print("Чтение интересной истории")

class StoryReader(): # у нас сейчас класс StoryReader напрямую зависит от класса Book, так не должно быть, они должны зависеть от абстракции
    def __init__(self, book):
        self.book = Book()

    def tell_story(self):
        self.book.read()

