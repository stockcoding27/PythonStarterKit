# 1. 숫자 연산 (산술 연산자)
a = 10
b = 3

print("덧셈:", a + b)        # 13
print("뺄셈:", a - b)        # 7
print("곱셈:", a * b)        # 30
print("나눗셈:", a / b)      # 3.333...
print("몫:", a // b)         # 3
print("나머지:", a % b)      # 1
print("거듭제곱:", a ** b)    # 1000

# 2. 비교 연산
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False

# 3. 논리 연산
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# 4. 문자열 연산
s1 = "안녕"
s2 = " 파이썬"

print(s1 + s2)         # 안녕 파이썬
print(s1 * 3)          # 안녕안녕안녕
print(len(s1))         # 2 (문자 개수)

# 5. 할당 연산자
x = 5
x += 3   # x = x + 3
print(x) # 8

x *= 2  # x = x * 2
print(x) # 16
