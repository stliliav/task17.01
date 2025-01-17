class Animal():
    def __init__(self):
        super().__init__()
class Dog(Animal):
    def prop(self):
        name = "Ruby"
        sound = "bark-bark"
        return name, sound
q = Dog()
print(f"Dog's name is {q.prop()[0]}, its sound is {q.prop()[1]}")
class Cat(Animal):
    def prop(self):
        name = "Chanel"
        sound = "miu-meow"
        return name, sound
w = Cat()
print(f"Cat's name is {w.prop()[0]}, its sound is {w.prop()[1]}")
        