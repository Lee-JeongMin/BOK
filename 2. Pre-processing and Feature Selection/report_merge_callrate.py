import pandas as pd
from datetime import datetime

report  = pd.read_csv('./report_preprocessing.csv')
callrate = pd.read_csv('../call_rate/call_rate_finish.csv')

# report의 date컬럼의 형식을 call금리의 date컬럼의 형식으로 맞춰주기(YYYY.MM.DD)
report['date'] = report['date'].apply(lambda x: datetime.strptime(x, '%y.%m.%d').strftime('%Y.%m.%d'))

# 콜금리 컬럼을 date와 label만 사용해서 merge하기
report_call = pd.merge(report, callrate[['date', 'label']], on='date')

# report와 call 금리 병합 데이터 저장하기
report_call.to_csv('./report_merge_callrate.csv', index=False)