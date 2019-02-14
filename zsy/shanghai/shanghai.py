# -*- coding:utf-8 -*-
import requests, sys, csv, json
reload(sys)
sys.setdefaultencoding('utf8')
for i in range(int(raw_input('几页'))):
    formdata = {'projectName': '', 'pageNo': i + 1, 'houseResourceType': '', 'regionName': '', 'priceleast': '','pricemax': '', 'arealeast': '', 'areamax': '', 'rentType': '', 'houserType': '', 'fitment': '','order': 1, 'asc': 1, }
    res = json.loads(requests.post('https://www.shzfzl.gov.cn/HouseInfo/getHouseInfo', data=formdata, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}).content)
    csv_write = csv.writer(open('res.csv', 'a'), dialect='excel')
    for i in res['dataInfo']['info']:
        csv_write.writerow([i['blockName'], i['communityAddress'], i['area'], i['price'], i["rentType"]])
