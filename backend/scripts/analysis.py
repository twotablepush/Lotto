import pandas as pd
import numpy as np

processed_path = "/Users/lsm/Desktop/study/Lotto/backend/data/processed/"
data = pd.read_excel(processed_path + "Lotto_processed.xlsx")

# 전체 회차 가장 많이 나온 숫자
most_all = data.iloc[:, 1:7].values.flatten()
most_all_counts = pd.Series(most_all).value_counts()
print("가장 많이 나온 숫자")
print(most_all_counts)

# 최근 5회 가장 많이 나온 숫자
most_recent_5 = data.iloc[-5:, 1:7].values.flatten()
most_recent_5_counts = pd.Series(most_recent_5).value_counts()
print("최근 5회 가장 많이 나온 숫자")
print(most_recent_5_counts)

# 최근 10회 가장 많이 나온 숫자
most_recent_10 = data.iloc[-10:, 1:7].values.flatten()
most_recent_10_counts = pd.Series(most_recent_10).value_counts()
print("최근 10회 가장 많이 나온 숫자")
print(most_recent_10_counts)

# 최근 15회 가장 많이 나온 숫자
most_recent_15 = data.iloc[-15:, 1:7].values.flatten()
most_recent_15_counts = pd.Series(most_recent_15).value_counts()
print("최근 15회 가장 많이 나온 숫자")
print(most_recent_15_counts)

num_range = set(range(1, 46))

# 최근 5회 등장하지 않은 숫자
absent_recent_5 = num_range - set(most_recent_5)
print("최근 5회 등장하지 않은 숫자:", sorted(absent_recent_5))

# 최근 10회 등장하지 않은 숫자
absent_recent_10 = num_range - set(most_recent_10)
print("최근 10회 등장하지 않은 숫자:", sorted(absent_recent_10))

# 최근 15회 등장하지 않은 숫자
absent_recent_15 = num_range - set(most_recent_15)
print("최근 15회 등장하지 않은 숫자:", sorted(absent_recent_15))

# 당첨숫자의 간격
data["평균간격"] = data.iloc[:, 1:7].apply(lambda row: np.mean(np.diff(sorted(row))), axis = 1)
print("숫자간 평균 간격 : ")
print(data[["회차", "평균간격"]].head())

# 홀/짝 비율

# 연속된 숫자

# 당첨숫자의 합계

# 드문 조합 랜덤

# 역사적 데이터 추세 분석

# 숫자간 상관관계 분석

# 가중치 기반 번호 선택