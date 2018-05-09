# 主目录下的Spider文件，需要放入对应的存放目录进行工作

import urllib.request
import re
import os


def fetch_pictures(url):
    global count
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<img class="BDE_Image" src="(.*?)"')
    picture_url_list = r.findall(html_content.decode('utf-8'))

    # os.mkdir('longzhu')
    os.chdir(os.path.join(os.getcwd(), ''))
    for i in range(len(picture_url_list)):
        picture_name = str(count) + '.jpg'
        count += 1
        urllib.request.urlretrieve(picture_url_list[i], picture_name)
        print("Success to download Image " + str(count) + " src = " +
              picture_url_list[i])


if __name__ == '__main__':
    global count
    count = 11412
    for i in range(1, 7):
        print("Downloading page " + str(i))
        print("Preparing for the Image " + str(count + 1))
        fetch_pictures("https://tieba.baidu.com/p/5685636816?pn=" + str(i))
    print("Preparing for the Image " + str(count + 1))    
