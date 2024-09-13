class Dog:

    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_color(self):
        return self.__color

    def set_age(self, age):
        self.__age = age

    def dark(self):
        return f'Собака {self.get_name}, возраста {self.get_age()}, цвета {self.get_color()} гавкает громко'


class Thoroughbred(Dog):

    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.__breed = breed

    def get_breed(self):
        return self.__breed

