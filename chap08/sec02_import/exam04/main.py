# import sub1, sub2

from sub1 import fun_a as sub1_fun_a, A as AClass
from sub2 import fun_b as sub2_fun_b, B as BClass

if __name__ == "__main__":
    # 모듈의 함수 호출
    sub1_fun_a()
    sub2_fun_b()
    
    # 모듈의 클래스를 이용해서 객체 생성
    obj_a = AClass()
    obj_b = BClass()