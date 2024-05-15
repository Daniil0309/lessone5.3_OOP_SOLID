# Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)

# class Bird():
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print("Птица летает")
#
# class Pinguin(Bird):
#     pass
#
# p = Pinguin("Пингвин")
#
# p.fly()

class Bird():   # Базовый класс
    def fly(self):
        print("эта птица летает")

class Duck(Bird): # Потомок базавого класса
    def fly(self):
        print("эта утка летает быстро")
# У нас получилось что базовый класс и патомок взаимозаменяемые
def fly_in_the_sky(animal):
    animal.fly()

b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)
