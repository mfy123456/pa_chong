# ending: utf-8

from bs4 import BeautifulSoup
import requests
import json

def get_page(): # 得到页面
    # 1、url
    url = "https://movie.douban.com/"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)<br>"
                     " Chrome/73.0.3683.86 Safari/537.36",
    }  # 伪造请求头
    # 请求GET/POST
    response = requests.get(url, headers=headers)  #发送请求
    #print(response.text) # 获取页面代码
    text = response.text
    print(text)
    return text

def parse_page(text):  # 解析页面
    soup = BeautifulSoup(text,'lxml') # 如果使用lxml不能够解析则使用html5lib
    lilist = soup.find_all('li',attrs={"data-enough":"true"})
    movies = []

    for li in lilist:
        movie = {}
        title = li['data-title']
        director = li["data-director"]
        region = li["data-region"]
        release = li["data-release"]
        actors = li["data-actors"]
        img = li.find("img")
        img_addr = img["src"]
        movie["title"] = title
        movie["director"] = director
        movie["region"] = region
        movie["release"] = release
        movie["actors"] = actors
        movie["img_addr"] = img_addr
        movies.append(movie)
    return movies

def save_data(data):

    with open('douban.json','w',encoding='utf-8') as fg:
# json.dump作用  encoding指定打开的编码格式
#将字典、列表dump成满足json格式的字符串
        json.dump(data,fg,ensure_ascii=False) #将ascii定为False





if __name__ == '__main__':
    text = get_page()
    movies = parse_page(text)
    save_data(movies)