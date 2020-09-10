import pandas as pd
from ekonlpy.tag import Mecab
from ekonlpy.sentiment import MPCK

pdf = pd.read_csv('pdf_2005_2017.csv', index_col=0)

# 필요한 컬럼만 남기기
pdf = pdf[['date', 'title', 'content']]
# print(len(pdf))

pdf['ngram'] = ''

for idx , sent in zip(pdf.index, pdf['content']):
    if (idx % 10) == 0:
        print('{}번째 끝'.format(idx)) 
  
    mpck = MPCK()

    # mpck.tokenize를 사용해 논문에서 사용하는 5개의 품사만 추출해 토큰화 한다. => uni-gram
    tokens = mpck.tokenize(sent)
    # pdf.loc[idx, 'token'] = tokens

    # mpck.ngramize를 사용해 bi-gram ~ 5-gram까지 ngram을 나눈다.
    ngrams = mpck.ngramize(tokens)
    # pdf.loc[idx, 'ngrams'] = ngrams

    # 'token'컬럼과 '2-5gram'을 합쳐서 '1~5'그램을 만든다.
    pdf['ngram'][idx] = tokens+ngrams

pdf.to_csv('./report_preprocessing.csv', index=False)