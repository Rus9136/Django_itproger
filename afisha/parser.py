import requests
from bs4 import BeautifulSoup
import sqlite3
from sqlite3 import Error


def parse():
    url = 'https://sxodim.com/shymkent/afisha'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='impression-card')

    list = []
    imgUrl = "https://sxodim.com/uploads/posts/2022/04/01/optimized/365accf67f76599663f7ae61f0f33339_352x198-q-85.jpg"
    path_to_image = imgUrl[imgUrl.find(":") + 50:]
    # p = requests.get(imgUrl)
    # out = open("static\img\img_"+path_to_image, "wb")
    # out.write(p.content)
    # out.close()

    for i in items:
        title = i.find(class_='impression-card-image').find('img').attrs['alt']
        date = i.find(class_='impression-card-info')


        list.append({'title': title, 'date': date.text.strip(), 'path_to_image': path_to_image})



    return list








parse()


