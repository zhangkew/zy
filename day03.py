# 一
import requests

URLS = []
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
URLS = HTML.split('\n')
lines = HTML.split('\n')

for url in URLS:
    response = requests.get(url)
    content = response.content
    name = url.split('/')[-1]
    with open(name,'wb')as f:
        f.write(content)



# 二
import requests
url = 'http://www.3wyu.com/wp-content/uploads/54903514201008070013271061944756556_001-1024x614.jpg'
res = requests.get(url)
HTML = res.text
URLS = HTML.split('\n')
for url in URLS:
    name = url.split('/')[-1]
    print(name)
    response = requests.get(url)
    content = response.content
    with open(res,'wb')as f:
        f.write(content)
    break