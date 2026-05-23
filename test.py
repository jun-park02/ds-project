import pandas as pd

df = pd.read_csv("시도_합계출산율__모의_연령별_출산율_20260520112924.csv", header=[0, 1])
df.head()

# 합계출산율 열만 선택
tfr = df.loc[:, df.columns.get_level_values(1) == "합계출산율"]
# 컬럼명을 연도만 남기기
tfr.columns = tfr.columns.get_level_values(0)
# 시도별을 인덱스로 지정
tfr.index = df[("시도별", "시도별")]

tfr