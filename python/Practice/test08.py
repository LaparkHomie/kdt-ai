# from math import pi as p
#
# print(p)

import urllib.request as r
response = r.urlopen('http://www.google.co.kr/')

print(response.status)
print(response)
print(response.read())
