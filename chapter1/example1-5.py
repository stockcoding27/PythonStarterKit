for i in range(5):
    print(f"{i}번째 반복입니다.")

print("-" * 40)

loop_count = 0
while True:
    if loop_count > 10:
        print(f"loop_count: {loop_count}으로 while문 탈출!")
        break
    loop_count += 1

print("-" * 40)

stocks = ["삼성전자", "LG에너지솔루션", "셀트리온", "네이버", "현대차"]

for stock in stocks:
    if stock in ["삼성전자", "셀트리온"]:
        print(f"⚠️ 금지 종목 '{stock}' 발견 → 건너뜁니다.")
        continue  # 더 이상 아래 부분으로 가지 않고 다음 loop로 넘어 갑니다.
    print(f"✅ 정상 종목: {stock}")


stock_name_to_code_dict = dict(
    삼성전자="005930",
    키움증권="039490",
)

for key, value in stock_name_to_code_dict.items():
    print(f"{key}: {value}")
