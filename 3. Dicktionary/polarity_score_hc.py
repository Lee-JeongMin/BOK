
df = pd.read_csv('total_up_down.csv')

count_up = 1670
count_down = 1914
count_total = count_up + count_down
df=df.replace(0,0.00001) # 0인 값 0.00001로 바꾸기

#polar_score 구하기
score = []
for i in range(len(df)):
    try:
        bnja = df['up_count'][i]/df['total_count'][i]/(up_count/total_count)
        bnmo = df['down_count'][i]/df['total_count'][i]/(down_count/total_count)
        tmp_score= bnja/bnmo
        score.append(tmp_score)
    except:
        print("0값이 있습니다.")       
df['polar_score'] = score


polarity = []
for i in range(len(df)):    
    if df.polar_score[i] > (1.3/1):
        tmp_polarity ='Hawkish'
    elif df.polar_score[i] < (1/1.3):
        tmp_polarity = 'Dovish'
    else:
        tmp_polarity= 'nothing'
    polarity.append(tmp_polarity)
df['polarity'] = polarity
df.polarity.value_counts()


df.query("down_count == 0.00001") # down_count인 값 0으로 대체하기
