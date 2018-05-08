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
    count = 10949
    for i in range(7, 9):
        print("Downloading page " + str(i))
        print("Preparing for the Image " + str(count + 1))
        fetch_pictures("https://tieba.baidu.com/p/4480274467?pn=" + str(i))
    print("Preparing for the Image " + str(count + 1))    
