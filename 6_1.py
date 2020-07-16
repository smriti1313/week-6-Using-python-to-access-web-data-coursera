import urllib.request,urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum=0
url=input('enter-')
js=urllib.request.urlopen(url,context=ctx).read()
info=json.loads(js)
# print('user count:',len(info['comments']))

for item in info['comments']:
    # print("count:",item['count'])
    sum+=int(item['count'])
print(sum)
