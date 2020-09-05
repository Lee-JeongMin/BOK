from tika import parser
from crawl_pdfurl import title_ls, name_ls, date_ls, pdf_ls
import pandas as pd
import pdftotext

def tika(pdf_url):

    PDFfileName = pdf_url
    parsed = parser.from_file(PDFfileName)

    return parsed["content"]

res = []

for idx, pdf in enumerate(pdf_ls):
    print(idx, pdf)

    text = tika(pdf)

    if text != None:
        text = text.replace('\n','').replace('\t','')

    res.append(text)

pdf_df = pd.DataFrame({'title':title_ls,'company':name_ls, 'date':date_ls, 'link':pdf_ls, 'content':res})

# Nan값인 행을 삭제
pdf_df = pdf_df.dropna(axis=0)
pdf_df.to_csv('./pdf_2005_2017.csv')