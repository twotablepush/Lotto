import pandas as pd
import numpy as np

# 데이터 로드
data = pd.read_excel("/Users/lsm/Desktop/study/Lotto/backend/data/raw/Lotto_data.xlsx")

# 데이터 확인
print("원본 데이터:")
print(data.head())  # 상위 5개 행 출력