# import sub1, sub2

import sub1 as s1
import sub2 as s2



if __name__ == "__main__":
    # 모듈의 함수 호출
    s1.fun_a()
    s2.fun_b()
    
    # 모듈의 클래스를 이용해서 객체 생성
    obj_a = s1.A()
    obj_b = s2.B()