import math

# 원주율 이용
def circle_area(r: float) -> float:
    return math.pi * r**2
print(circle_area(3))

# 보다 큰 정수
print(math.ceil(2.3))   # 3

# 보다 적은 정수
print(math.floor(2.3))  # 2

# 반올림
print(round(2.3))   # 2