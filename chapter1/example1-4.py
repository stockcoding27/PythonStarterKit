score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("등급: A")
elif score >= 80:
    print("등급: B")
elif score >= 70:
    print("등급: C")
elif score >= 60:
    print("등급: D")
else:
    print("등급: F")


user_id = input("아이디를 입력하세요: ")
user_pw = input("비밀번호를 입력하세요: ")

if user_id == "admin" and user_pw == "1234":
    print("로그인 성공!")
elif user_id == "admin":
    print("비밀번호가 틀렸습니다.")
else:
    print("아이디가 존재하지 않습니다.")