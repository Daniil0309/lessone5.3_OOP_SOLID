# Принцип открытости/закрытости (OCP, Open/Closed Principle)

# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrint(self):
#         print(f"сформированный отчет - {self.title} - {self.content}")

from abc import ABC, abstractmethod

# Определяем абстрактный базовый класс Formatter
class Formatter(ABC):
    @abstractmethod
    def format(self, report):
        pass

# Конкретный класс TextFormatter, который наследуется от Formatter
class TextFormatter(Formatter):
    # Метод format принимает объект report и выводит его заголовок и содержимое в текстовом формате
    def format(self, report):
        print(report.title)
        print(report.content)

# Конкретный класс HtmlFormatter, также наследуется от Formatter
class HtmlFormatter(Formatter):
    # Метод format принимает объект report и выводит его заголовок и содержимое в HTML-формате
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")

# Класс Report представляет отчет и содержит его заголовок, содержимое и объект форматирования
class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    # Метод docPrinter вызывает метод format объекта форматирования для отчета
    def docPrinter(self):
        self.formatted.format(self)


# Создаем объект класса Report с заданным заголовком, содержимым и объектом форматирования TextFormatter
report = Report("Заголовок отчета", "это текст отчета. его тут много", TextFormatter())
# Вызываем метод docPrinter для отчета, который выводит его в заданном формате
report.docPrinter()