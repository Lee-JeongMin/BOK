import pandas as pd

df_1 = pd.read_csv('./dataset/article_call.csv')
df_2 = pd.read_csv('./dataset/report_merge_callrate.csv')
df_3 = pd.read_csv('./dataset/minutes_with_label.csv')

# 뉴스 & 채권분석리포트 & 금통위 의사록 합치기
news_report_mpb = pd.concat([df_1, df_2, df_3])
news_report_mpb.to_csv('./dataset/news_report_mpb.csv')

news_report_mpb = pd.read_csv('./dataset/news_report_mpb.csv')

def cnt_value(df, col_name):

    tot_cnt = df['ngram'].str.split(expand=True).stack().value_counts().to_frame(name=col_name)
    tot_cnt = tot_cnt.reset_index().rename(columns={"index": "ngram"})

    return tot_cnt

u_DF = news_report_mpb.loc[news_report_mpb['label']== 'up']
d_DF = news_report_mpb.loc[news_report_mpb['label']== 'down']

# up_count 컬럼 생성
up_df = cnt_value(u_DF, 'up_count')
# down_count 컬럼 생성
down_df = cnt_value(d_DF, 'down_count')

# up_count과 down_count을 병합한 후 더해서 total_count 컬럼 생성
up_down_df = pd.merge(up_df,down_df, on='ngram', how='outer')
up_down_df = up_down_df.fillna(0)
up_down_df['total_count'] = up_down_df['up_count']+up_down_df['down_count']

is_above_15 = up_down_df['total_count'] >= 15
up_down_tot_df = up_down_df[is_above_15]

up_down_tot_df.to_csv('./dataset/re_total_up_down.csv',index=False)