from tika import parser
from crawl_pdfurl import title_ls, name_ls, date_ls, pdf_ls
import pandas as pd

def pdftotext(pdf_url):

    PDFfileName = pdf_url
    parsed = parser.from_file(PDFfileName)

    return parsed["content"]

res = []

for idx, pdf in enumerate(pdf_ls):
    print(idx, pdf)

    text = pdftotext(pdf)
    res.append(text)

pdf_df = pd.DataFrame({'title':title_ls,'company':name_ls, 'date':date_ls, 'link':pdf_ls, 'content':res})
pdf_df.to_csv('./pdf_2012_2017.csv')