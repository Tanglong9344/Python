import requests

upload_url = 'http://localhost:8089/api/uploadFile.do'
print('upload url:', upload_url)
# 打开文件
filePath = 'E:\\pythonProject\\paperCheck\\test.pdf'
with open(filePath, 'rb') as f:
    files = {'file': ('test.pdf', open(filePath, 'rb'))}
    try:
        response = requests.post(url=upload_url, files=files)
        print("response:", response.json())
        response.close()
    except Exception as e:
        print("upload error:", e)