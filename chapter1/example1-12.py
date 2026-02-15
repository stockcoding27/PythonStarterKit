class Lecture:
    def __init__(self, name, open_date=''):  # 생성자
        self.name = name  # 인스턴스 변수
        self.open_date = open_date
        self.do_introduction()

    def do_introduction(self):
        self.introduce()

    def introduce(self):  # 메서드
        print(f"안녕하세요, {self.name} 강의에 오신 것을 환영합니다. 강의 개설일은 {self.open_date}입니다.")


class OnlineLecture(Lecture):  # Lecture 클래스를 상속
    def __init__(self, name, open_date=''):
        super().__init__(name, open_date)  # 부모 클래스 생성자 호출

    def introduce(self):  # 메서드 오버라이딩
        print("[온라인 강의 안내]")
        print(f"개설일은 {self.open_date}입니다. 많은 참여 바랍니다.")

# 객체 생성
lecture = Lecture("파이썬", open_date="2025-05-21")

print("-" * 40)

# 객체 생성
online_lecture = OnlineLecture("자동매매 기초", open_date="2025-08-01")


