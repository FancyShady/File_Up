import requests

url = 'http://127.0.0.1:8080/publish/script_upload'

files = {
    'file': ('Redis-x64-3.0.504.zip', open('E:\\ ', 'rb'))
}

data = {
    'fileServiceId': 'test'
}

r = requests.post(url, data=data, files=files, headers={'token': ''})
print(r.json())
