import numpy as np

# 0) 버전 확인 (재현성 체크)
print("NumPy:", np.__version__)

# 1) 배열 생성과 dtype/shape
a = np.array([1, 2, 3])                     # 파이썬 리스트 → 1차원 배열
b = np.array([[1.0, 2.0], [3.0, 4.0]])      # 2차원 배열 (float)
z = np.zeros((2, 3))                         # 0으로 채운 배열
o = np.ones((2, 3), dtype=np.int32)          # 1로 채운 배열 + 정수 dtype
ar = np.arange(0, 10, 2)                     # [0, 2, 4, 6, 8]
lin = np.linspace(0, 1, 5)                   # 0~1 구간 5등분

print(a.shape, a.dtype)  # (3,) int64(플랫폼에 따라 다름)
print(b.shape, b.dtype)  # (2, 2) float64
print(z)
print(o)
print(ar)
print(lin)

# 2) 인덱싱/슬라이싱/뷰(view)
c = np.array([10, 11, 12, 13, 14])
print(c[0], c[-1])           # 10, 14
print(c[1:4])                # [11 12 13]

# 슬라이스는 "뷰"라서 원본에 영향
s = c[1:4]
s[0] = 99
print(c)                     # [10 99 12 13 14]

# 3) 벡터화(루프 없이 계산)와 ufunc
x = np.arange(1, 6)          # [1 2 3 4 5]
y = x**2 + 2*x + 1           # 다항식 벡터화
print(y)                     # [ 4  9 16 25 36]
print(np.sqrt(y))            # ufunc 예시

# 4) 집계(aggregation)와 axis
A = np.array([[1, 2, 3],
              [4, 5, 6]])
print(A.sum())               # 전체 합: 21
print(A.sum(axis=0))         # 열 합: [5 7 9]
print(A.mean(axis=1))        # 행 평균: [2. 5.]

# 5) 불리언 인덱싱 & 조건 연산
data = np.array([3, 7, 2, 9, 4, 8])
mask = data > 5
print(mask)                  # [False  True False  True False  True]
print(data[mask])            # [7 9 8]
data[data % 2 == 0] = -1
print(data)                  # 짝수는 -1로 치환

# 6) 타입 변환과 안전한 연산
f = np.array([1.2, 2.8, 3.5], dtype=np.float32)
i = f.astype(np.int32)
print(f.dtype, i, i.dtype)
