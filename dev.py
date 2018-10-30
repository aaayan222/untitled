import requests
from bs4 import BeautifulSoup

from pysql import MySQLCommand

mysqlCommand = MySQLCommand()
mysqlCommand.connectMysql()

with open('zhuimeiju.txt', 'w', encoding='utf-8') as f:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    for i in range(1, 16):
        url = 'http://www.aizhuiju.com/Mov/rank/movie/upTime/Pn' + str(i)
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        for i in soup.find_all("div", class_="movies"):
            for right in i.find_all(class_="right"):  # 获取全部right标签成为一个列表
                name = right.find("h4").a.get_text(strip=True)
                print(name)
                li = right.find_all('ul')  # 将每个right标签下的ul标签获取为列表
                # td = [x for x in li]  # 获取的列表
                # print(list(right.find_all("ul"))[0].get_text(strip=True))
                # print(list(right.find_all("ul"))[0].text.strip().replace('\xa0', ''))
                type = li[0].get_text(strip=True)  # 直接从列表里取值
                actor = li[1].get_text(strip=True)
                score = li[2].get_text(strip=True)
                date = li[3].get_text(strip=True)
                print(type, actor, score, date)
                # score = right.find(attrs={"class": "score"}).a.get_text(strip=True)
                cols = {"name", "type", "actor", "score", "date"}
                try:
                    add = mysqlCommand.insertData(name, type, actor, score, date)
                    if add:
                        dataCount = add
                except Exception as e:
                    print("插入数据失败", str(e))  # 输出插入失败的报错语句
