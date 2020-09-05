import numpy as np
from selenium import webdriver

page = np.arange(1,105)
title_ls, name_ls, date_ls, pdf_ls = [], [], [], []

driver = webdriver.Chrome('./chromedriver.exe')
for p in page:
    url = "https://finance.naver.com/research/debenture_list.nhn?keyword=&brokerCode=&searchType=writeDate&writeFromDate=2005-01-01&writeToDate=2017-12-31&x=42&y=22&page="+str(p)
    driver.get(url)

    #제목 정보 수집
    titles = driver.find_elements_by_xpath('//*[@id="contentarea_left"]/div[3]/table[1]/tbody/tr/td[1]/a')
    #증권사
    names = driver.find_elements_by_xpath('//*[@id="contentarea_left"]/div[3]/table[1]/tbody/tr/td[2]')
    #pdf 링크
    links = driver.find_elements_by_xpath('//*[@id="contentarea_left"]/div[3]/table[1]/tbody/tr/td[3]/a')
    #날짜 이름 수집
    dates = driver.find_elements_by_xpath('//*[@id="contentarea_left"]/div[3]/table[1]/tbody/tr/td[4]')

    for n in range(len(titles)):
        title_ls.append(titles[n].text)
        name_ls.append(names[n].text)
        date_ls.append(dates[n].text)
        pdf_ls.append(links[n].get_attribute("href"))

    print(str(p)+' page 끝')
driver.close()