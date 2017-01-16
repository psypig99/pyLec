def add_number(*number):
    total = 0
    for a in number:
        total += a
    print(total)

add_number(10)
add_number(10, 20)
add_number(10,20,30,40,50)