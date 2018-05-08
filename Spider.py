# 爬取贴吧龙珠图片,网址：http://tieba.baidu.com/p/3720487356

import urllib.request
import re
import os


def fetch_pictures(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<img class="BDE_Image" src="(.*?)"')
    picture_url_list = r.findall(html_content.decode('utf-8'))

    # os.mkdir('longzhu')
    os.chdir(os.path.join(os.getcwd(), ''))
    for i in range(len(picture_url_list)):
        picture_name = str(i) + '.jpg'
        try:
            urllib.request.urlretrieve(picture_url_list[i], picture_name)
            print("Success to download " + picture_url_list[i])
        except:
            print("Fail to download " + picture_url_list[i])

if __name__ == '__main__':
    for i in range(1, 56):
        fetch_pictures("https://tieba.baidu.com/p/5629404210?pn="+str(i))