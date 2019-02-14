import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
with open('resault.txt','rb+') as fil:
    content=json.loads(fil.read())
    with open('resaultfinal.txt','a') as fi:
        for i in content["content"]["positionResult"]["result"]:
            fi.write(i["positionName"].ljust(10)+i["workYear"].ljust(10)+i["salary"].ljust(10)+i["companyFullName"].ljust(30)+i["positionAdvantage"]+'   '.join(i["companyLabelList"])+'\n')
