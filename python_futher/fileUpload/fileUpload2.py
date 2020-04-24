import requests
from urllib3 import encode_multipart_formdata

upload_url = 'http://localhost:8089/api/uploadFile.do'
print('upload url:', upload_url)
# 打开文件
filePath = 'E:\\pythonProject\\paperCheck\\test.pdf'
with open(filePath, 'rb') as f:
    form_data = {
        'p1': '1',
        'p2': '2',
        'p2': '3',
    }
    encode_data = encode_multipart_formdata(form_data)
    print('encode_data[1]:', encode_data[1])
    headers = {
        # 'Content-Type': encode_data[1],
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    files = {'file': ('test.pdf', open(filePath, 'rb'))}
    try:
        response = requests.request('POST',url=upload_url, files=files,data=form_data,headers=headers)
        print("response:", response.json())
        response.close()
    except Exception as e:
        print("upload error:", e)