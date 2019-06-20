from urllib.parse import urlencode
from urllib.request import urlopen, Request

# get 방식
http_response = urlopen('http://www.example.com?a=10&b=20')
body = http_response.read()
print(body)

print('=====================================')

# post 방식
data = {
    'email' : 'leeap1004@gmail.com',
    'password' : '1234',
    'name':'이정은'
}
data = urlencode(data).encode('utf-8')
request = Request('http://www.example.com', data)

request.add_header('Content-Type', 'text/html')
request.add_header('cookies:jsessionid=3232dswsd2')

http_response = urlopen(request)
body = http_response.read()
print(body)