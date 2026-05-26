# import sub1, sub2

from sub1 import fun_a, A
from sub2 import fun_b, B

if __name__ == "__main__":
    # 모듈의 함수 호출
    fun_a()
    fun_b()
    
    # 모듈의 클래스를 이용해서 객체 생성
    obj_a = A()
    obj_b = B()