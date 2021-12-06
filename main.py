# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Bird(object):

    def __init__(self, name, species, movement):
        self.name = name
        self.species = species
        self.movement = movement

    def display(self):
        print("My name is {}".format(self.name))
        print("I am a {}".format(self.species))
        print("I get around by {}".format(self.movement))


bird1 = input("Enter a name for your first bird: ")
print("Your first bird is named ", bird1)
bird2 = input("Enter a name for your second bird: ")
print("Your second bird is named", bird2)

bird1 = Bird(bird1, "bird", "flying")
bird2 = Bird(bird2, "bird", "flying")

bird1.display()
bird2.display()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
