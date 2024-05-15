# # Принцип инверсии зависимости (DIP, Dependency Inversion Principle)
#
# class Book():
#     def read(self):
#         print("Чтение интересной истории")
#
# class StoryReader(): # у нас сейчас класс StoryReader напрямую зависит от класса Book, так не должно быть, они должны зависеть от абстракции
#     def __init__(self, book):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read()

from abc import ABC, abstractmethod

class StorySource(ABC):  # Абстрактный базовый класс от которого все зависит
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource): #это источники которые заваисят от нашео абстрактного базового класса
    def get_story(self):
        print("Чтение интересной истории")

class AudioBook(StorySource):#это источники которые заваисят от нашео абстрактного базового класса
    def get_story(self):
        print("Чтение интересной аудио истории вслух")


class StoryReader(): # и есть класс  StoryReader который использует источники
    def __init__(self, story_source):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story() # story_source это источник который у нас будет выбираться

book = Book()
audioBook = AudioBook()

readerBook = StoryReader(book)

readerAudioBook = StoryReader(audioBook)

readerBook.tell_story()
readerAudioBook.tell_story()

