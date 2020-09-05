# BOK

### 한국 은행 논문을 구현합니다.
이정민 조현채 문인균 박광덕

#### 1. Preparing Corpus

* 데이터 목록
  * [금통위 의사록](https://www.bok.or.kr/portal/bbs/B0000245/list.do?menuNo=200761)
  * [뉴스 기사](https://search.naver.com/search.naver?where=news&sm=tab_jum&query=금리)
  * [채권분석 리포트](https://finance.naver.com/research/debenture_list.nhn)
  * [콜금리](https://finance.naver.com/marketindex/interestDetail.nhn?marketindexCd=IRR_CALL)
* 수집 기간 
  * 2005년 1월 1일 ~ 2017년 12월 31일



#### 2. Pre-Processing & Feature Selection

**eKoNLPy 사용해 구현**

* Tokenize 
  * POS Tagging 
  * Lemmatization 
  * Replacing Synonyms 
* Ngramize
  * "Noun, Adjective, Adverb, Verb, Negation" 총 5개의 품사만 사용
  * unigram ~ 5-gram까지 15번 이상 등장하는 단어만 사용  
  * 

#### 3. Polaity Classification



#### 4. Sentiment Measurement





