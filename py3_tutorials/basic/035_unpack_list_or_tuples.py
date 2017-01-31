# item = ["December 10, 2015", "Bread", 10]

# date, item, cost = ["December 10, 2015", "Bread", 10]
# print(date)
# print(item)
# print(cost)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

grades = [56, 55, 98, 39, 78]
grades.sort()
print(grades)
drop_first_last(grades)
