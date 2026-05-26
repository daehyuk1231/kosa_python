# 명령행으로 직접 실행했을 경우
import sys


if __name__ == "__main__":
    print(type(sys.argv), sys.argv)
    if len(sys.argv) <= 2:
        sys.exit(0)

    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
        
    print("sum:", sum)