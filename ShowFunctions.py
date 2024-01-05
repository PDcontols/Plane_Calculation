import pandas as pandas
import numpy as numpy

col1 = pandas.Series([1, 2, 3, 4, 5, 6], index=["C_xa_i", "C_xa_wing", "C_xa_stab", "C_xa_tail", "C_xa_body", "C_xa_pods"])

data = {'Value': col1}

df = pandas.DataFrame(data)
print(df)
df.head()