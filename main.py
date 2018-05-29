# класс животные
class Animal:
  def __init__(self, sound, size, name, speed):
    self.sound = sound
    self.size  = size
    self.name  = name
    self.name  = speed

  def getVoice(self):
    return self.name + ' говорит ' + self.sound

  def __str__(self):
    return "This is a %s" % (self.name)

  def move(self, coordinates):
    pass

# летающие 
class Flying:
  pass

# Корова
class Cow(Animal):
  pass

# коза
class Goat(Animal):
  pass

# свинья
class pig(Animal):
  pass

# Овца
class Sheep(Animal):
  pass

# курица
class Hen(Animal):
  pass

# утка
class Duck(Animal, Flying):
  pass

# гусь
class Goose(Animal, Flying):
  pass
 