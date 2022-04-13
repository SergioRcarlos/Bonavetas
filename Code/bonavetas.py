#!/usr/bin/env python3

import pandas as pd

#res = pd.read_csv("DS0731-Test.txt")
res = pd.read_csv("DS0731.txt")

print(res)

print('')

print(res[['Game','LuckyMonth']].head(2))

#print('\n')
print('')

print(res.iloc[2]['Game'])
print(res.iloc[2]['LuckyMonth'])

print('')

print(res.iat[0,0])
print(res.at[1,'LuckyMonth'])

print('')

print(res.at[res.index[-1],'LuckyMonth'])

print('')

print(res['LuckyMonth'].values[0])
