import math  # math 모듈: 수학 함수 제공

print(f"PI 값: {math.pi}")
print(f"제곱근(16): {math.sqrt(16)}")
print(f"5의 팩토리얼: {math.factorial(5)}")
print("-" * 40)

from math import pi, sqrt  # 필요한 함수만 선택해서 가져오기: from ~ import ~ 형식

print(f"PI 값: {pi}")
print(f"제곱근(25): {sqrt(25)}")
print("-" * 40)
import pandas as pd  # as를 이용한 별칭 사용
print(f"빈 데이터 프레임: {pd.DataFrame()}")

print("-" * 40)
from my_file import say_hello  # 직접 만든 my_file.py 파일에서 함수 import 가능
say_hello("홍길동")