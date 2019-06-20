from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

# 성공
# GET / HTTP/1.1
# 200 OK
conn.request('GET', '/')
response = conn.getresponse()
print(response.status, response.reason)

if response.status == 200:
    body = response.read()
    print(body, type(body))

print('----------------------------------')

# 실패
# GET /hello.html HTTP/1.1
# 404 File Not Found
conn.request('GET', '/hello.html')
response = conn.getresponse()
print(response.status, response.reason)

