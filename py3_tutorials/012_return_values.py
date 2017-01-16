def allowed_dating_age(my_age):
    girls_age = my_age/2+7
    return girls_age

joe_limit = allowed_dating_age(30)
chris_limit = allowed_dating_age(50)

print(joe_limit)
print(chris_limit)