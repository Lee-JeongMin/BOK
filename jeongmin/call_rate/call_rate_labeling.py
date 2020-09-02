import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

callrate = pd.read_csv('./call_rate.csv')

# 1. 날짜를 기준으로 정렬하기
callrate = callrate.sort_values(by=['date'])

def all_date_range_df(date_range):

    df2 = pd.DataFrame({'date':date_range})
    
    return df2

# 2. 비어있는 날짜와 금리를 추가하기
date_range = (pd.date_range(start='20041224', end='20200831')).strftime("%Y.%m.%d").tolist()
df2 = all_date_range_df(date_range)

def df_outer_join_merge(df1, df2):
    
    df_OUTER_JOIN = pd.merge(df1, df2, left_on='date', right_on='date', how='outer', sort=True)
    
    # 공휴일에 없는 환율정보는 전날을 기준으로 결측값 채우기
    df_finally = df_OUTER_JOIN.fillna(method='ffill')
    
    return df_finally

# 3. 두 df를 병합하고 결측값 채우기
fin_df = df_outer_join_merge(callrate, df2)
fin_df = fin_df.set_index('date')

# 4. 한달 전 날짜 추가하기
month_date = []
for target_date in fin_df.index:
    
    month_before = (datetime.strptime(target_date,'%Y.%m.%d' ) - relativedelta(months = 1)).strftime('%Y.%m.%d')
    month_date.append(month_before)
    
fin_df['month_date'] = month_date

# 5. 한달 전 날짜에 맞춰 콜 금리 추가하기
month_rate=[]
for target_date in fin_df['month_date']:
    try:
        rate = fin_df._get_value(target_date, 'callrate') 
        month_rate.append(rate)
    except: # keyError 제외
        month_rate.append(0.0)
fin_df['month_rate'] = month_rate

# 6. 콜 금리의 차이를 구하고 0 초과 : 'up', 0 같음 : 'same', 0 미만 : 'down'으로 라벨링
value_diff = fin_df['callrate'] - fin_df['month_rate']

fin_df['label']='0'
for i, diff in enumerate(value_diff):
    if diff > 0:
        fin_df['label'][i] = 'up'
    elif diff == 0:
        fin_df['label'][i] = 'same'
    elif diff < 0:
        fin_df['label'][i] = 'down'     

fin_df.reset_index(inplace=True)
fin_df.to_csv('call_rate_finish.csv')