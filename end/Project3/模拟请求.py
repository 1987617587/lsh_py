import requests

# res = requests.get('http://127.0.0.1:8000/categories/')
# print(res.json())
res = requests.post("https://m.mi.com/v1/home/page", headers={
    "Referer": "https://m.mi.com/"
})
print(res.json())
