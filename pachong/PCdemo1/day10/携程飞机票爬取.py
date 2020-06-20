import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Cookie': '_abtest_userid=b4ae7640-4395-4a53-993c-fb8050a42cd6; _ga=GA1.2.1151191299.1563862790; _RSG=qY4K5rNxOc24d39glbz.X8; _RDG=2846d858a8b1952291180216ecf3c3f7e3; _RGUID=2998ed7d-4550-48b4-887e-f65bea2439c4; __utma=1.1151191299.1563862790.1563863166.1563863166.1; MKT_CKID=1577183526451.i75n1.0e6t; DomesticUserHostCity=441|%c9%cc%c7%f0; gad_city=9be3213015a43ebad792c50d612d2d54; MKT_CKID_LMT=1585834855724; _gid=GA1.2.1775745197.1585834856; MKT_Pagesource=PC; FD_SearchHistorty={"type":"S","data":"S%24%u5317%u4EAC%28BJS%29%24BJS%242020-04-30%24%u5E7F%u5DDE%28%u767D%u4E91%u56FD%u9645%u673A%u573A%29%28CAN%29%24CAN"}; _gat=1; appFloatCnt=2; _RF1=42.238.153.236; _bfa=1.1572339833509.16w7bu.1.1585834852963.1585901374288.11.32; _bfs=1.2; _jzqco=%7C%7C%7C%7C1585834855882%7C1.1171688159.1572339835845.1585901379902.1585901393253.1585901379902.1585901393253.undefined.0.0.31.31; __zpspc=9.11.1585901379.1585901393.2%234%7C%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D101023%26v1%3D32%26v2%3D31',
    'content-type': 'application/json',
    'referer': 'https://flights.ctrip.com/itinerary/oneway/bjs-can?date=2020-04-30',
}
url = 'https://flights.ctrip.com/itinerary/api/12808/products'
payload = {
    "flightWay": "Oneway",
    "classType": "ALL",
    "hasChild": 'false',
    "hasBaby": 'false',
    "searchIndex": 1,
    "date": "2020-04-30",
    "airportParams": [
        {
            "dcity": "BJS",
            "acity": "CAN",
            "dcityname": "北京",
            "acityname": "广州",
            "date": "2020-04-30",
            "dcityid": 1,
            "acityid": 32
        }
    ],
    "token": "be030ce3f1f7cce352e6077543dcaa25"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
data = response.json()
print(data)