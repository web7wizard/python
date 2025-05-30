import numpy as np
import pandas as pd
data=np.array([1,3,6,7,8])
ser=pd.Series(data)
print(ser[:3])
print(ser[1])

"""
0    1
1    3
2    6
dtype: int64
3
"""