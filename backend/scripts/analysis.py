import pandas as pd

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