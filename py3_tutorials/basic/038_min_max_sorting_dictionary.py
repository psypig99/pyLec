"""
딕셔너리는 key, value 값을 가지고 있음
딕셔너리의 값을 정리하고자 함
하지만 파이썬에서 딕셔너리는 자체적으로 정렬을 할 수가 없음
"""

import operator

stocks = {
    "Samsung Eletronics" : 130,
    "NC" : 30.5,
    "LGE" : 7.5,
    "SKT" : 75.2
}
def printStock(stocks):
    for key, value in stocks:
        print(key, value)

# zip function은 자체 정렬 기능이 존재하고 있음
zipStocks = zip(stocks.values(), stocks.keys())
# printStock(zipStocks)

# print(min(zipStocks))
# printStock(zipStocks)
# print(max(zipStocks))
# print(sorted(zipStocks, key=operator.itemgetter(1), reverse=True))




