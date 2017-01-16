magicNumber = 35

# This program finds a magic number.

# for n in range(101):
#     if n is magicNumber:
#         print(n, " is the magic number")
#         break
#     print(n)

for n in range(1, 101):
    if n%4 is 0 and n >=30:
        print(n, " is a magic number")
    else:
        continue
