import pandas as pd
import numpy as np
import re
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

#Flight Number Emputation
lst = np.where(np.isnan(df['FlightNumber']))
df['FlightNumber'].iloc[lst]=10045+10*np.array(lst)
df['FlightNumber'] = df['FlightNumber'].astype('int32')

#From_to fix
df['From'] = df['From_To'].apply(lambda x:x.split('_')[0])
df['To'] = df['From_To'].apply(lambda x:x.split('_')[1])
df.drop(['From_To'],axis=1,inplace=True)

#Capitalization
df['From'] = df['From'].apply(lambda x:x.capitalize())
df['To'] = df['To'].apply(lambda x:x.capitalize())

#RecentDelays
max_delay_len = max(df['RecentDelays'].apply(lambda x:len(x)))
dx = df['RecentDelays'].apply(pd.Series)
dx.columns = ["delay_"+str(x+1) for x in range(max_delay_len)]
df = pd.concat([df,dx],axis=1)
df.drop(columns=['RecentDelays'],axis=1,inplace=True)

#Airline fix
df['Airline'] = df['Airline'].apply(lambda x:re.sub(r'\d+',"",re.sub(r'[^\w\s]','',x)))
print(df)
