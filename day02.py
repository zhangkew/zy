# 一
import urllib.request

url = 'http://www.baidu.com'

proxy_handle = {
    'http':'http://163.204.240.162:9999',
    'http':'http://113.67.231.143:5555',
}
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy)
request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request)
print(response.read())
while 1:
    print(response.status)
    if(response.status!=200):
        print('%爬虫失败')
    break 

# 二
import urllib.request
def read_pageHtml(url):
    file = urllib.request.urlopen(url)
    data = file.read()
    return data

url ='http://www.17k.com/chapter/2933095/36699279.html'
data = read_pageHtml(url)
print(data)

def storageToLocalfiles(urls,data):
    fhandle = open(urls,'wd')
    fhandle.write(data)
    fhandle.close()
urls = 'C:\Users\Administrator\Desktop'
data = storageToLocalFiles(urls,data)