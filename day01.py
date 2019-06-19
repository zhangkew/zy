import urllib.request
import urllib.parse


def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


url = 'http://baidu.com/post'
headers = {
 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
 'Host': 'baidu'
}
dict = {
 'name': 'Germey'
}

data = urllib.parse.urlencode({'wd':''})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)


data = bytes(urllib.parse.urlencode({'pw':'123','abc':'456'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)