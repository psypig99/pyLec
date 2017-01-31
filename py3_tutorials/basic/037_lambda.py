"""
lambda는 함수명이 존재하지 않으며 재활용성을 고려한 함수보다는
1회성으로 잠깐 사용하는 속성 함수라고 볼 수 있음
"""
answer = lambda x: x**3

print(answer(5))

power = list(map(lambda x: x**2, (range(1,6))))
print(power)