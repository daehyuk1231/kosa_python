import time

def sum(var1, var2):
    result = 0
    for i in range(var1, var2 + 1):
        result += i
    return result

# 시간 측정하기
start = time.time()
sum(1, 1000000)
end = time.time()
print(f"걸린시간: {end-start}초")

# 주기적으로 실행하기
while True:
    print("2초 간격으로 출력")
    time.sleep(2)