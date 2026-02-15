def say_hello(name, nickname=""):
    print(f"{name}, {nickname}님 안녕하세요!")

say_hello("지민")
say_hello("철수")

def calculate(a, b):
    sum_val = a + b
    product = a * b
    return sum_val, product

result = calculate(3, 4)  # (7, 12) 반환
print(result)
sum_result, product_result = calculate(3, 4)  # 값 분리
print(sum_result)
print(product_result)