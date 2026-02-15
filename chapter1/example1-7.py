# math 모듈: 수학 관련 함수 제공
import math

print("math 모듈 예제:")
print(f"절댓값: {abs(-5)}")
print(f"제곱근: {math.sqrt(16)}")
print(f"올림: {math.ceil(3.2)}")
print(f"내림: {math.floor(3.8)}")
print(f"파이: {math.pi}")
print("-" * 40)

# random 모듈: 난수 생성
import random

print("random 모듈 예제:")
print(f"0 이상 1 미만의 난수: {random.random()}")
print(f"1 이상 10 이하의 정수 난수: {random.randint(1, 10)}")
print(f"리스트에서 랜덤 선택: {random.choice(['a', 'b', 'c'])}")
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(f"리스트 셔플: {lst}")
print("-" * 40)

# datetime 모듈: 날짜와 시간
import datetime

print("datetime 모듈 예제:")
now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now}")
print(f"현재 연도: {now.year}")
print(f"현재 월: {now.month}")
print(f"현재 일: {now.day}")
print(f"날짜 계산 (3일 후): {now + datetime.timedelta(days=3)}")
print("-" * 40)

# time 모듈: 시간 측정, 대기
import time

print("time 모듈 예제:")
print(f"현재 시간 (timestamp): {time.time()}")
print("3초 대기 중...")
time.sleep(3)
print("대기 완료")
