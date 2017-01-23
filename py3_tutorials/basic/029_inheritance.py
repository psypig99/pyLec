class Parent():
    def print_last_name(self):
        print("Norman")

class Child(Parent):
    def print_first_name(self):
        print("Chris")

    def print_last_name(self):
        print("Hong")

chris = Child()
chris.print_first_name()
chris.print_last_name()
