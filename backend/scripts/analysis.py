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
print("최근 5회 등장하지 않은 숫자 : ", sorted(absent_recent_5))

# 최근 10회 등장하지 않은 숫자
absent_recent_10 = num_range - set(most_recent_10)
print("최근 10회 등장하지 않은 숫자 : ", sorted(absent_recent_10))

# 최근 15회 등장하지 않은 숫자
absent_recent_15 = num_range - set(most_recent_15)
print("최근 15회 등장하지 않은 숫자 : ", sorted(absent_recent_15))

# 당첨숫자의 간격
data["평균간격"] = data.iloc[:, 1:7].apply(lambda row: np.mean(np.diff(sorted(row))), axis = 1)
print("숫자간 평균 간격 : ")
print(data[["회차", "평균간격"]].head())

# 홀/짝 비율
data["홀수"] = data.iloc[:, 1:7].apply(lambda row: sum(num % 2 != 0 for num in row), axis = 1)
data["짝수"] = 6 - data["홀수"]
print("홀/짝 비율 : ")
print(data[["회차", "홀수", "짝수"]].head())

# 당첨숫자의 합계
data["합계"] = data.iloc[:, 1:7].sum(axis = 1)
print("당첨번호 합계 : ")
print(data[["회차", "합계"]].head())

# 연속된 숫자
def count_consecutive_numbers(row):
    sorted_row = sorted(row)
    count = 0
    for i in range(len(sorted_row) - 1):
        if sorted_row[i + 1] - sorted_row[i] == 1:
            count += 1
    return count
data["연속된숫자"] = data.iloc[:, 1:7].apply(count_consecutive_numbers, axis = 1)
print("연속된 숫자 개수 : ")
print(data[["회차", "연속된숫자"]].head())

# 숫자간 상관관계 분석

# 가중치 기반 번호 선택