import pandas as pd
import numpy as np

# 데이터 로드
data = pd.read_excel("/Users/lsm/Desktop/study/Lotto/backend/data/raw/Lotto_data.xlsx")

# 번호 범위 (1 ~ 45)
num_range = np.arange(1, 46)

# 각 회차의 번호를 원-핫 인코딩
one_hot_encoded = data.iloc[:, 1:7].apply(
    lambda row: np.isin(num_range, row).astype(int), axis = 1
)

# 원-핫 결과를 데이터프레임으로 변환
one_hot_df = pd.DataFrame(
    np.vstack(one_hot_encoded),
    columns=[f"번호_{i}" for i in range(1, 46)]
)

# 기존 데이터와 결합
final_data = pd.concat([data, one_hot_df], axis = 1)

# 결합된 데이터 확인
print("\n최종 데이터:")
print(final_data.head())