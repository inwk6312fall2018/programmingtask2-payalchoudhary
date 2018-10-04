import pandas as pd
df = pd.read_csv("Crime.csv", parse_dates = ['EVT_DATE'], usecols=['RUCR','RUCR_EXT_D','EVT_DATE'])
#df1 = (df,header=0, names = ['CRIME ID','CRIME NAME','CRIME DATE'])
df= df.rename(columns={'RUCR': 'CRIME ID','RUCR_EXT_D': 'CRIME NAME','EVT_DATE': 'CRIME DATE'})
df=df.set_index('CRIME ID')
df=df.sort_values(by ='CRIME DATE')
print(df)
