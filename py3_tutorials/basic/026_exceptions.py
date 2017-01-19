# ans = int(input("What yout fav number?\n"))
# print(ans)

while True :
    try:
        number = int(input("What yout fav number?\n"))
        print(23/number)
        break
    # except ValueError:
    #     print("장난쳐??")
    # except ZeroDivisionError:
    #     print("0으로는 나눌 수 없습니다 ")
    except:
        print("빠져나갑니다~~~")
        break
    finally:
        print("빠져나가도 이거는 해야지~~~~")
