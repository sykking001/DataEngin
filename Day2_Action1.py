import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_content(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(url, headers=headers, timeout=10)
    content = html.text
    return content

def parse_table(content, columns, df):
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    # 找到完整的投诉信息框
    temp = soup.find('div', class_="tslb_b")
    # 创建DataFrame

    tr_list = temp.find_all('tr')
    for tr in tr_list[1:]:
        td_list = tr.find_all('td')
        temp = {}
        column_index = 0
        for td in td_list:
            temp[columns[column_index]] = td.text
            column_index += 1
        df = df.append(temp, ignore_index=True)
    return df
sum_pages = 5
page = 1
columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status']
df = pd.DataFrame(columns=columns)


while sum_pages > 0:
    url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-' + str(page) + '.shtml'
    content = get_content(url)
    df = parse_table(content, columns, df)
    print('Page '+str(page)+ ' is finished')
    sum_pages -= 1
    page += 1


print(df)
df.to_excel('汽车投诉数据.xlsx', index=False)