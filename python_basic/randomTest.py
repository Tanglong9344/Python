import random
import requests

source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
boundary='----'
for i in range(0,34):
    boundary += random.choice(source)
print(boundary)

str2 = b'------CP0DJiFI1jzkPYnXbUYdwHS9SkTU1iQ16c\r\nContent-Disposition: form-data; name="async_request"\r\nContent-Type: multipart/form-data\r\n\r\n1\r\n------CP0DJiFI1jzkPYnXbUYdwHS9SkTU1iQ16c\r\nContent-Disposition: form-data; name="author_first"\r\nContent-Type: multipart/form-data\r\n\r\nnone\r\n------CP0DJiFI1jzkPYnXbUYdwHS9SkTU1iQ16c\r\nContent-Disposition: form-data; name="author_last"\r\nContent-Type: multipart/form-data\r\n\r\nnone\r\n------CP0DJiFI1jzkPYnXbUYdwHS9SkTU1iQ16c\r\nContent-Disposition: form-data; name="title"\r\nContent-Type: multipart/form-data\r\n\r\ntest.pdf\r\n------CP0DJiFI1jzkPYnXbUYdwHS9SkTU1iQ16c--\r\n'
print(str2)
print(str(str2,'utf-8'))

str3 = '/newreport.asp?r=80.3769661128165&svr=26&lang=zh_hans&oid=1312973616&pbd=2&ft=1&ro='
print(str3.split('oid=')[1].split('&')[0])

str4 = 'javascript:void(0);'
subStr = 'javascript:void(0);'
if subStr in str4:
    print('yes')

# headers = {'Host': 'ev.turnitin.com',
#            'Cookie': 'legacy-session-id=72891fe6dea09f4ba49d1c13f5a29325; session-id=72891fe6dea09f4ba49d1c13f5a29325'}
# oid = '1281691845'
# option_url = 'https://ev.turnitin.com/student/paper/%s/options?lang=zh_hans&cv=1&output=json&tl=0'%oid
# option_data={"exclude_quotes":0,"id":"%s_0"%oid,"exclude_small_matches":-1,"translate_language":0,"paper":int(oid),"exclude_biblio":1}
# response = requests.put(option_url, data=option_data, headers=headers)
# statusCode = response.status_code
# print('status code:', statusCode)
# print('result:',response.json())

a = [1,2,3]
print(a[0:len(a)-1])

s = 'https://zero.sci-hub.se/7098/1c3a2e1c306a4d1fac2f69d87e5e878c/dunk2018.pdf?download=true'
print(s.split('/')[2])

list = [1,2,3,4,5]
list2 = list.copy()
list = []
print('list:',list)
print('list2:',list2)