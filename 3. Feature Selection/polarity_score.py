import pandas as pd
import numpy as np

df_1 = pd.read_csv('./dataset/article_call.csv')
df_2 = pd.read_csv('./dataset/report_merge_callrate.csv')
df_3 = pd.read_csv('./dataset/minutes_with_label.csv')

# 뉴스 & 채권분석리포트 & 금통위 의사록 합치기
news_report_mpb = pd.concat([df_1, df_2, df_3])

# 결측값있는 행 제거
news_report_mpb = news_report_mpb.dropna(axis=0)
news_report_mpb.to_csv('./dataset/news_report_mpb.csv')

# news_report_mpb = pd.read_csv('./dataset/news_report_mpb.csv')

def cnt_value(df, col_name):

    tot_cnt = df['ngram'].str.split(expand=True).stack().value_counts().to_frame(name=col_name)
    tot_cnt = tot_cnt.reset_index().rename(columns={"index": "ngram"})

    return tot_cnt

u_DF = news_report_mpb.loc[news_report_mpb['label']== 'up']
d_DF = news_report_mpb.loc[news_report_mpb['label']== 'down']

# polar_score 구할때 사용
len_u_DF = len(u_DF)
len_d_DF = len(d_DF)

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

# polar_score 식
p_dovish = len_d_DF/ (len_d_DF+len_u_DF)
p_hawkish = len_u_DF/ (len_d_DF+len_u_DF)

p_ngram_dovish = total_up_down['down_count']/total_up_down['total_count']
p_ngram_hawkish = total_up_down['up_count']/total_up_down['total_count']

total_up_down['polar_score'] = (p_dovish * p_ngram_hawkish) / (p_hawkish * p_ngram_dovish)

# polar_score > 1.3 : Hawkish / polar_score < 0.76 : Dovish / 0.76 <= polar_score <= 1.3 : nothing
total_up_down['polarity'] = np.where(total_up_down['polar_score'] > 1.3, 'Hawkish', np.where(total_up_down['polar_score'] < 0.76, 'Dovish', 'nothing' ))

# 긍정(Hawkish)/부정(Dovish)로 나눠서 사전 저장하기
pos_dict = total_up_down.query("polarity == 'Hawkish'")
neg_dict = total_up_down.query("polarity == 'Dovish'")

pos_dict.to_csv('./dataset/pos_dict.csv',index=False) 
neg_dict.to_csv('./dataset/neg_dict.csv',index=False) 
# Hawkish(pos): 1617건 Dovish(neg) : 2591건  nothing : 3675건