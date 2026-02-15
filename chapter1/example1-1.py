stock_name = "삼성전자"  # 문자열 ('삼성전자'와 차이 없음)
current_price = 60000  # 정수
체결강도 = 120.3  # 실수
is_buy_signal = False  # 불리언
none_value = None  # None 타입

# 출력
print(stock_name)
print(current_price)
print(체결강도)
print(is_buy_signal)
print(none_value)

print(type(stock_name))  # <class 'str'>
print(type(current_price))  # <class 'int'>
print(type(체결강도))  # <class 'float'>
print(type(is_buy_signal))  # <class 'bool'>
print(type(none_value))  # <class 'NoneType'>

# 추가 팁: f-string으로 출력 예쁘게 하기
print(f"{stock_name}의 현재가는 {current_price}, 체결강도는 {체결강도}입니다.")