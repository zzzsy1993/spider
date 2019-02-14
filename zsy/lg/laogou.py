# -*- coding:utf-8 -*-

import requests, json, csv, urllib, sys

reload(sys)
sys.setdefaultencoding('utf8')


class LaSpider(object):
    def __init__(self):
        self.base_url = 'https://www.lagou.com/jobs/positionAjax.json'
        self.headers = {

            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "43",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "WEBTJ-ID=20180607110913-163d83839834c9-08fe17ccb20613-3e70055f-838992-163d83839844dd; user_trace_token=20180607110914-28375ac8-6a00-11e8-9381-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_pq%3Dbc980cc700023e9e%26rsv_t%3Da512RQUB%252FB%252F9DaPu2DBBhRO3BxZIm2PV8Eb0zEB4sRm%252BvIjbIOduimm6ASY%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D6%26rsv_sug1%3D6%26rsv_sug7%3D101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGUID=20180607110914-28375efe-6a00-11e8-9381-5254005c3644; X_HTTP_TOKEN=e54dfae937099e0115eda3a9e23547dc; JSESSIONID=ABAAABAACBHABBI251B0781B9568A6E83D72433BBA6B430; _putrc=2B4413D1DBF74254123F89F2B170EADC; login=true; unick=%E5%A4%8F%E7%BE%8E%E7%BE%8E; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=cf9b132ca427c49f35bee739b809affd88d5e28e50b3fb844380ca3234c134a8; _gid=GA1.2.1533868501.1528340954; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528340954; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528341306; _ga=GA1.2.1715448506.1528340954; LGSID=20180607110914-28375d40-6a00-11e8-9381-5254005c3644; LGRID=20180607111505-f9c94591-6a00-11e8-9381-5254005c3644; TG-TRACK-CODE=search_code; SEARCH_ID=8b50d3bb02a94f4cbd96d3390b35b21a; index_location_city=%E5%85%A8%E5%9B%BD",
            "Host": "www.lagou.com",
            "Origin": "https://www.lagou.com",
            "Referer": "https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?px=default&city=%E6%9D%AD%E5%B7%9E",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36",
            "X-Anit-Forge-Code": "0",
            "X-Anit-Forge-Token": "None",
            "X-Requested-With": "XMLHttpRequest"

        }

        self.city_name = raw_input('请输入需要抓取的城市')
        self.work_name = raw_input('请输入需要抓取的职位')
        self.page_num = int(raw_input('请输入需要抓取的页数'))
        self.page = 1

    def send_request(self):
        formdata = {
            "first": "true",
            "pn": self.page,
            "kd": self.work_name
        }
        parame_data = {
            "px": "default",
            "city": self.city_name,
            "needAddtionalResult": "false"
        }

        kwstr = urllib.urlencode(formdata)
        self.headers["Content-Length"] = str(len(kwstr))

        try:
            response = requests.post(self.base_url, params=parame_data, data=formdata, headers=self.headers)
            return response

        except Exception as e:
            print e

    def write(self, content):
        # with open('a.json','w') as fil:
        #     fil.write(content)
        content = json.loads(content)
        with open('res.csv', 'a') as fi:
            csv_write = csv.writer(fi, dialect='excel')
            for i in content["content"]["positionResult"]["result"]:
                lis = [i["positionName"], i["workYear"], i["salary"], i[
                    "companyFullName"], i["positionAdvantage"], ''.join(i["companyLabelList"])]
                csv_write.writerow(lis)

    def manage(self):
        for i in range(self.page_num):
            self.write(self.send_request().content)
            self.page += 1


if __name__ == '__main__':
    a = LaSpider()
    a.manage()
