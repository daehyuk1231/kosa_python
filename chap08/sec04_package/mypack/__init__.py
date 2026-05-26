# 현재 패키지에 있는 모듈들을 *로 가져올 경우
# from mypack import *
from . import module1, module2
__all__ = ["module1", "module2"]

# 특정 모듈에 있는 함수를 가져올 경우
# from mypack import fun
from .module1 import fun