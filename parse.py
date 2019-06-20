from urllib.parse import urlparse

# full url 파싱
result = urlparse('http://www.python.org:80/guide/python.html:philosophy?overall=3#here')
print(result)