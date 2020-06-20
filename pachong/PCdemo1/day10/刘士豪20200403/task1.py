'''
https: // flights.ctrip.com /
案例：协程机票的爬取
爬取有关城市、机场、航站楼、航空公司、航班、航空器信息、机票价格等信息
'''

import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Cookie': '_abtest_userid=b4ae7640-4395-4a53-993c-fb8050a42cd6; _ga=GA1.2.1151191299.1563862790; _RSG=qY4K5rNxOc24d39glbz.X8; _RDG=2846d858a8b1952291180216ecf3c3f7e3; _RGUID=2998ed7d-4550-48b4-887e-f65bea2439c4; __utma=1.1151191299.1563862790.1563863166.1563863166.1; MKT_CKID=1577183526451.i75n1.0e6t; DomesticUserHostCity=441|%c9%cc%c7%f0; gad_city=9be3213015a43ebad792c50d612d2d54; MKT_CKID_LMT=1585834855724; _gid=GA1.2.1775745197.1585834856; MKT_Pagesource=PC; FD_SearchHistorty={"type":"S","data":"S%24%u5317%u4EAC%28BJS%29%24BJS%242020-04-30%24%u5E7F%u5DDE%28%u767D%u4E91%u56FD%u9645%u673A%u573A%29%28CAN%29%24CAN"}; _gat=1; appFloatCnt=2; _RF1=42.238.153.236; _bfa=1.1572339833509.16w7bu.1.1585834852963.1585901374288.11.32; _bfs=1.2; _jzqco=%7C%7C%7C%7C1585834855882%7C1.1171688159.1572339835845.1585901379902.1585901393253.1585901379902.1585901393253.undefined.0.0.31.31; __zpspc=9.11.1585901379.1585901393.2%234%7C%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D101023%26v1%3D32%26v2%3D31',
    'content-type': 'application/json',
    'referer': 'https://flights.ctrip.com/itinerary/oneway/bjs-can?date=2020-04-30',
}
# url = 'https://flights.ctrip.com/itinerary/api/12808/products'
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
# print(data['data']['routeList'][0])
routeList = data['data']['routeList']
for route in routeList:
    # print(route['legs'][0])
    flight = route['legs'][0]['flight']
    print(f'flight:{flight}')
    # 航班id
    id = flight['id']
    # 航班编号
    print(f'id:{id}')
    flightNumber = flight['flightNumber']
    print(f'flightNumber:{flightNumber}')
    airlineCode = flight['airlineCode']
    print(f'airlineCode:{airlineCode}')
    airlineName = flight['airlineName']
    print(f'airlineName:{airlineName}')

    craftTypeCode = flight['craftTypeCode']
    print(f'craftTypeCode:{craftTypeCode}')
    craftKind = flight['craftKind']
    print(f'craftKind:{craftKind}')
    craftTypeName = flight['craftTypeName']
    print(f'craftTypeName:{craftTypeName}')
    craftTypeKindDisplayName = flight['craftTypeKindDisplayName']
    print(f'craftTypeName:{craftTypeKindDisplayName}')
    print("from")
    # 出发城市信息
    departureAirportInfo = flight['departureAirportInfo']
    cityTlc = departureAirportInfo['cityTlc']
    print(f'cityTlc:{cityTlc}')
    cityName = departureAirportInfo['cityName']
    print(f'cityName:{cityName}')
    airportTlc = departureAirportInfo['airportTlc']
    print(f'airportTlc:{airportTlc}')
    airportName = departureAirportInfo['airportName']
    print(f'cityTlc:{airportName}')
    # 航站楼信息
    terminal = departureAirportInfo['terminal']
    terminal_id = terminal['id']
    print(f'terminal_id:{terminal_id}')
    terminal_name = terminal['name']
    print(f'terminal_name:{terminal_name}')
    terminal_shortName = terminal['shortName']
    print(f'terminal_shortName:{terminal_shortName}')
    print("end")
    # 目标达到城市信息
    arrivalAirportInfo =  flight['arrivalAirportInfo']
    cityTlc = arrivalAirportInfo['cityTlc']
    print(f'cityTlc:{cityTlc}')
    cityName = arrivalAirportInfo['cityName']
    print(f'cityName:{cityName}')
    airportTlc = arrivalAirportInfo['airportTlc']
    print(f'airportTlc:{airportTlc}')
    airportName = arrivalAirportInfo['airportName']
    print(f'cityTlc:{airportName}')
    # 航站楼信息
    terminal = arrivalAirportInfo['terminal']
    terminal_id = terminal['id']
    print(f'terminal_id:{terminal_id}')
    terminal_name = terminal['name']
    print(f'terminal_name:{terminal_name}')
    terminal_shortName = terminal['shortName']
    print(f'terminal_shortName:{terminal_shortName}')

    # 时间信息
    departureDate = flight['departureDate']
    print(f'departureDate:{departureDate}')
    arrivalDate = flight['departureDate']
    print(f'arrivalDate:{arrivalDate}')
    # 价格信息
    cabins = route['legs'][0]['cabins']
    print(f'len:{len(cabins)}')
    for cabin in cabins:
        id = cabin['id']
        print(f'id:{id}')
        price = cabin['price']['price']
        print(f'price:{price}')
    print('='*66)