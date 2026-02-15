# 예제 1: 0으로 나누기
try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

# 예제 2: 문자열을 숫자로 변환
try:
    num = int("abc")
except ValueError:
    print("정수로 변환할 수 없는 값입니다.")

# 예제 3: 리스트 인덱스 오류
try:
    items = [1, 2, 3]
    print(items[5])
except IndexError:
    print("리스트 인덱스 범위를 벗어났습니다.")

# 예제 4: 딕셔너리 키 오류
try:
    person = {"name": "Alice"}
    print(person["age"])
except KeyError:
    print("존재하지 않는 키입니다.")

# 예제 5: 여러 예외 처리
try:
    x = int("100")
    y = x / 0
except Exception as e:
    print(e)