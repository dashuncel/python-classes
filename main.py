# суперкласс животные
class Animal:

    def __init__(self, sound, size, name, speed):
        self.sound = sound
        self.size = size
        self.name = name
        self.speed = speed

    def get_voice(self):
        return self.name + ' говорит ' + self.sound

    def __str__(self):
        return "Знакомьтесь, это %s" % (self.name)

    def move(self, coordinates):
        pass


# суперкласс летающие
class Flying:

    def start_fly(self, height, speed):
        return '{} взлетает на высоту {} метров со скоростью {} метров \
                в минуту'.format(self.name, height, speed)


# Корова
class Cow(Animal):

    def __init__(self, size, name, speed, milk):
        super().__init__("mu-mu", size, name, speed)
        self.milk = milk

    def __str__(self):
        return "Это %s, которая дает %s литров молока в день" % \
               (self.name, self.milk)

    def add_milk(self, milk):
        self.milk += milk
        return self.milk


# коза
class Goat(Animal):

    def __init__(self, size, name, speed):
        super().__init__("me-me", size, name, speed)


# свинья
class Pig(Animal):

    def __init__(self, size, name, speed):
        super().__init__("hryu-hryu", size, name, speed)


# Овца
class Sheep(Animal):

    def __init__(self, size, name, speed):
        super().__init__("be-be", size, name, speed)


# курица
class Hen(Animal):

    def __init__(self, size, name, speed, eggs):
        super().__init__("ko-ko", size, name, speed)
        self.egg = eggs

    def __str__(self):
        return "Это %s, которая несет %s яиц в день" % (self.name, self.egg)

    def add_egg(self, eggs):
        self.egg += eggs
        return self.egg


# утка
class Duck(Animal, Flying):
    def __init__(self, size, name, speed):
        super().__init__("me-me", size, name, speed)


# гусь
class Goose(Animal, Flying):
    def __init__(self, size, name, speed):
        super().__init__("ga-ga-ga", size, name, speed)


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
