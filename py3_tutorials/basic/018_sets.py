shopping_list = {
    "stapler", "milk", "eggs", "beer", "water", "beef", "duct tape", "milk", "beer"
}

print(shopping_list)

item = input("Which one do you need?")
if item in shopping_list:
    print("You already have milk in the list")
else:
    print("Yeah~ You need to put it")
