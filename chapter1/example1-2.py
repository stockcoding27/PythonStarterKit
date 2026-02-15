# 📌 리스트 (List)
print("▶ 리스트 예제")
stocks_list = ["삼성전자", "키움증권", "SK하이닉스"]
print(f"원본 리스트: {stocks_list}")

stocks_list.append("현대차")
print(f"추가 후: {stocks_list}")

print(f"첫 번째 값: {stocks_list[0]}")
print(f"리스트 길이: {len(stocks_list)}")
print(f"키움증권의 index값: {stocks_list.index('키움증권')}")

print("-" * 40)


# 📌 딕셔너리 (Dictionary)
print("▶ 딕셔너리 예제")
stock_name_to_code_dict = dict(
    삼성전자="005930",
    키움증권="039490",
)
# 또는 아래와 같이 해도 됨
# stock_name_to_code_dict = {
#     "삼성전자": "005930",
#     "키움증권": "039490",
# }

print(f"원본 딕셔너리: {stock_name_to_code_dict}")
stock_name_to_code_dict["SK하이닉스"] = "000660"  # SK하이닉스 데이터 추가

print(f"추가 후: {stock_name_to_code_dict}")
삼성전자_종목코드 = stock_name_to_code_dict["삼성전자"]  # 삼성전자에 대해 데이터를 찾고 없으면 KeyError
현대차_종목코드 = stock_name_to_code_dict.get("현대차", "")  # 현대차에 대해 데이터를 찾고, 없으면 "" 을 반환 (KeyError를 피할 수 있음)


del stock_name_to_code_dict["삼성전자"]
print(f"삭제 후: {stock_name_to_code_dict}")

print(f"키 목록: {list(stock_name_to_code_dict.keys())}")
print(f"값 목록: {list(stock_name_to_code_dict.values())}")
print("-" * 40)


# 📌 집합 (Set)
print("▶ 집합 예제")
stock_set = {"삼성전자", "키움증권", "SK하이닉스"}
stock_set.add("현대차")  # 현대차 추가
print(f"추가 후 집합: {stock_set}")
stock_set.remove("키움증권")
print(f"삭제 후 집합: {stock_set}")
print("-" * 40)
