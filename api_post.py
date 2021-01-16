import requests

# url: Đường dẫn web api, ví dụ: "http://127.0.0.1:8000/"
# payload: Chuỗi Json chứa dữ liệu, ví dụ: {'category': 'Hehe', 'name': 'hoho','price': '10'}
# files: Kiểu List, ví dụ: []
# headers: Kiểu Dictionary, ví dụ: {}

def response_data(url, payload, files, headers):
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text + " -> Done!")

