from Parent import Parent

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)
        print("Child class is initialized")

    def play(self):
        print(f"{self.name} is playing.")
