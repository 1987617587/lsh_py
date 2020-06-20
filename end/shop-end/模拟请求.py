import requests,time

for i in range(1000):
    res = requests.get("http://127.0.0.1:8000/api/v1/categorys/")
    print(time.time(), "当前",i)
    print(res.json())

# for i in range(1000):
#     res = requests.post("https://m.mi.com/v1/home/page", headers={
#         "Referer": "https://m.mi.com/"
#     })
#     print(time.time(), "当前",i)
#     print(res.json())