
import requests
import re
x=requests.post("https://www.w3schools.com/")
y=x.text
z= r'<a\s+.*?</a>'
b=re.findall(z, y)

for i in b:
    print(i)

