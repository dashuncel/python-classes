# суперкласс животные
class Animal:

    sound = ''

    def __init__(self, size, name, speed):
        self.size = size
        self.name = name
        self.speed = speed

    def get_voice(self):
        return self.name + ' говорит ' + self.sound

    def __str__(self):
        return "Знакомьтесь, это %s" % self.name

    def move(self, coordinates):
        pass


# суперкласс летающие
class Flying:

    def start_fly(self, height, speed):
        return '{} взлетает на высоту {} метров со скоростью {} метров в минуту'.format(self.name, height, speed)


# Корова
class Cow(Animal):

    def __init__(self, size, name, speed, milk):
        self.sound = "mu-mu"
        self.milk = milk
        super().__init__(size, name, speed)

    def __str__(self):
        return "Это %s, которая дает %s литров молока в день" % \
               (self.name, self.milk)

    def add_milk(self, milk):
        self.milk += milk
        return self.milk


# коза
class Goat(Animal):

    def __init__(self, size, name, speed):
        self.sound = "me-me"
        super().__init__(size, name, speed)


# свинья
class Pig(Animal):

    def __init__(self, size, name, speed):
        self.sound = "hryu-hryu"
        super().__init__(size, name, speed)


# Овца
class Sheep(Animal):

    def __init__(self, size, name, speed):
        self.sound = "be-be"
        super().__init__(size, name, speed)


# курица
class Hen(Animal):

    def __init__(self, size, name, speed, eggs):
        self.sound = "ko-ko"
        self.egg = eggs
        super().__init__(size, name, speed)

    def __str__(self):
        return "Это %s, которая несет %s яиц в день" % (self.name, self.egg)

    def add_egg(self, eggs):
        self.egg += eggs
        return self.egg


# утка
class Duck(Animal, Flying):
    def __init__(self, size, name, speed):
        self.sound = "me-me"
        super().__init__(size, name, speed)


# гусь
class Goose(Animal, Flying):
    def __init__(self, size, name, speed):
        self.sound = "ga-ga-ga"
        super().__init__(size, name, speed)


# экземпляры классов:
goose = Goose(10, "goose", 100)
print(goose)
print(goose.get_voice())

duck = Duck(15, "duck", 50)
print(duck)
print(duck.start_fly(100, 100))

hen = Hen(11, "little chicken", 50, 10)
print(hen)

cow1 = Cow(110, "my little cow - 1", 20, 30)
cow2 = Cow(120, "my little cow - 2", 20, 25)
print(cow1)
print(cow2)

goat = Goat(20, 'my little goat', 10)
print(goat)

my_pig = Pig(200, 'my little pig', 10)
print(my_pig)

my_sheep = Sheep(80, 'my little sheep', 10)
print(my_sheep)
