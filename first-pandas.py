import pandas as pd

#y = pd.read_excel("year.xlsx", sheet_name="Sheet1")
y = pd.read_csv("year.csv") \
    .merge(pd.read_csv("yearmap.csv"), how='left', on='Year')

#c = pd.read_excel("city.xlsx", sheet_name="Sheet1")
c = pd.read_csv("city.csv") \
    .merge(pd.read_csv("citymap.csv"), how='left', on='City')

merge = pd.merge(c, y, how='outer', on=['Firstname','Lastname'])
