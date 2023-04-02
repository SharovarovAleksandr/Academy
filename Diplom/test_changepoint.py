import pandas as pd
import numpy as np
from datetime import datetime, timedelta


df=pd.read_csv('GBPCAD_D1_new.csv', delimiter=';')
df['time']=pd.to_datetime(df['time'])
# for i in range(len(df)):
#     df.loc[i, 'up'] = df['up_fractal'][i]
#     df.loc[i, 'dn'] = df['down_fractal'][i]

# change_lst = []
# j = 0
# i = 0
#
# while i <= len(df)-1 or j <= len(df)-1:
#
#     if df['up_fractal'][i] > 0 and not df['down_fractal'][i] > 0:
#         temp_lst_up = []
#         j = i
#         temp_lst_up.append([i, df['up_fractal'][i]])
#         while not df['down_fractal'][j] > 0:
#             j += 1
#             if j >= len(df):
#                 break
#             if df['up_fractal'][j] > 0:
#                 temp_lst_up.append([j, df['up_fractal'][j]])
#         if j >= len(df):
#             change_lst.append(df['time'][i])
#             break
#         if df['up_fractal'][j] > 0:
#             temp_lst_up.append([j, df['up_fractal'][j]])
#
#         if len(temp_lst_up) == 1:
#             change_lst.append(df['time'][i])
#             i+=1
#             continue
#         else:
#             max_up = temp_lst_up[0][1]
#             indx=temp_lst_up[0][0]
#             for m in temp_lst_up:
#                 if m[1] > max_up:
#                     max_up = m[1]
#                     indx = m[0]
#             for m in temp_lst_up:
#                 if m[0] != indx:
#                     df.loc[m[0], 'up_fractal']=np.NaN
#
#                 else:
#                     change_lst.append(df['time'][indx])
#         i = j
#         continue
#
#     if df['down_fractal'][i] > 0 and not df['up_fractal'][i] > 0:
#         temp_lst_down = []
#         j = i
#         temp_lst_down.append([i, df['down_fractal'][i]])
#         while not df['up_fractal'][j] > 0:
#             j += 1
#             if j >= len(df):
#                 break
#             if df['down_fractal'][j] > 0:
#                 temp_lst_down.append([j, df['down_fractal'][j]])
#         if j >= len(df):
#             change_lst.append(df['time'][i])
#             break
#         if df['down_fractal'][j] > 0:
#             temp_lst_down.append([j, df['down_fractal'][j]])
#
#         if len(temp_lst_down) == 1:
#             change_lst.append(df['time'][i])
#             i+=1
#             continue
#         else:
#             min_dn = temp_lst_down[0][1]
#             indx = temp_lst_down[0][0]
#             for m in temp_lst_down:
#                 if m[1] < min_dn:
#                     min_dn = m[1]
#                     indx = m[0]
#             for m in temp_lst_down:
#                 if m[0] != indx:
#                     df.loc[m[0], 'down_fractal'] = np.NaN
#
#                 else:
#                     change_lst.append(df['time'][indx])
#         i = j
#         continue
#
#     if df['down_fractal'][i] > 0 and df['up_fractal'][i] > 0:
#
#         j = i
#         while not (df['down_fractal'][j+1] > 0) and not (df['up_fractal'][j+1] > 0):
#             j += 1
#             if j >= len(df):
#                 break
#         j+=1
#         if j >= len(df):
#             change_lst.append(df['time'][i])
#             break
#         if df['down_fractal'][j] > 0 and not df['up_fractal'][j] > 0:
#             # change_lst.append(df['time'][i])
#             df.loc[i, 'down_fractal'] = np.NaN
#
#         if df['up_fractal'][j] > 0 and not df['down_fractal'][j] > 0:
#             # change_lst.append(df['time'][i])
#             df.loc[i, 'up_fractal'] = np.NaN
#
#         if df['down_fractal'][j] > 0 and df['up_fractal'][j] > 0:
#
#             if df['down_fractal'][i] < df['down_fractal'][j] and df['up_fractal'][i] > df['up_fractal'][j]:
#                 df.loc[j, 'down_fractal'] = np.NaN
#                 df.loc[j, 'up_fractal'] = np.NaN
#
#             if df['down_fractal'][i] > df['down_fractal'][j] and df['up_fractal'][i] < df['up_fractal'][j]:
#                 df.loc[i, 'down_fractal'] = np.NaN
#                 df.loc[i, 'up_fractal'] = np.NaN
#
#             if df['down_fractal'][i] < df['down_fractal'][j] and df['up_fractal'][i] < df['up_fractal'][j]:
#                 df.loc[i, 'up_fractal'] = np.NaN
#
#
#                 # change_lst.append(df['time'][i])
#                 # i=j
#             if df['down_fractal'][i] > df['down_fractal'][j] and df['up_fractal'][i] > df['up_fractal'][j]:
#                 df.loc[i, 'down_fractal'] = np.NaN
#
#                 # change_lst.append(df['time'][i])
#                 # i=j
#         continue
#     i += 1
#

# change_lst=set(change_lst)
# change_lst=list(change_lst)
# change_lst.sort()

# for i in range(len(df)):
#     if df['time'][i] in change_lst:
#         df.loc[i, 'change_lst'] = df['time'][i]
#     else:
#         df.loc[i, 'change_lst'] = np.NaN

# df.to_csv('GBPCAD_D1_chang.csv', sep=';')

# df_new=pd.DataFrame(columns=['ds', 'y', 'change_point'])
df_new=pd.DataFrame()
start = df['time'][0]
end = df['time'][len(df)-1]

df_new['ds']= pd.date_range(start, end, freq='d')
i=0
j=0
mark='high'
while i<len(df_new):
    if df_new['ds'][i] == df['time'][j]:
        df_new.loc[i, mark] = df[mark][j]
        df_new.loc[i, 'holiday'] = np.NaN
        df_new.loc[i, 'holiday_day'] = np.NaN
        i += 1
        j += 1
    else:
        i_new=i
        while df_new['ds'][i_new] != df['time'][j]:
            df_new.loc[i_new, 'holiday'] = 'holiday'
            df_new.loc[i_new, 'holiday_day'] = df_new['ds'][i_new]
            i_new+=1
        delta=i_new-i
        delta_mark=df[mark][j] - df[mark][j-1]
        m=1
        for k in range(i,i_new):
            df_new.loc[k, mark] = df[mark][j-1] + m*delta_mark/(delta+1)
            m+=1
        # j+=1
        i=i_new
print(df_new)