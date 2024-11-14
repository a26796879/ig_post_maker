import pdfplumber # type: ignore
import re
import random

pdf = pdfplumber.open('kotoba.pdf')

sentense_list = []

for p in range(len(pdf.pages)):
    page = pdf.pages[p]           # 讀取第二頁
    text = page.extract_text_lines()
    for t in text:
        pattern = re.compile(r'(\d+) (.*)') # type: ignore
        match = pattern.match(t['text'])
        if match:
            sentense_list.append(match.group(2))
            #print(match.group(2))
print(random.choice(sentense_list))
pdf.close()