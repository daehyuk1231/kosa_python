# import sub1, sub2

import sub1
import sub2

if __name__ == "__main__":
    # 모듈의 함수 호출
    sub1.fun_a()
    sub2.fun_b()
    
    # 모듈의 클래스를 이용해서 객체 생성
    obj_a = sub1.A()
    obj_b = sub2.B()