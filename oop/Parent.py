class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Parent class is initialized")


    def talk(self):
        print(f"{self.name} is talking!")


    def eat(self):
        print(f"{self.name} is eating!")


    def get_info(self):
        print(f"{self.name} is {self.age} years old!")
