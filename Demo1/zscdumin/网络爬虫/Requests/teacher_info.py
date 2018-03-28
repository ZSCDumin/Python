# 湖南大学导师信息爬虫

import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"


def getInfoList(infoList, url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    urls = soup.find_all('a')
    for url in urls:
        try:
            href = str(url.attrs['href'])[5:]  # 获取照片路径
            if ".htm" and "info" in href:
                infoList.append(href)
        except:
            continue


def printInfoList(infoList, fPath):
    i = 1
    for info in infoList:
        r = requests.get("http://csee.hnu.edu.cn" + info)
        path = fPath + "teacherInfo" + str(i) + ".html"  # 拼接文件路径
        with open(path, 'wb') as f:  # 写入文件
            f.write(r.content)
            f.close()
            print("文件保存成功")
        i = i + 1


def main():
    infoList = []  # 图片URL列表
    fPath = "G://湖大复试//导师信息//"  # 图片存储路径
    url = "http://csee.hnu.edu.cn/xygk/szll/jsjkxx.htm"  # 爬取页面URL
    getInfoList(infoList, url)
    printInfoList(infoList, fPath)


main()
