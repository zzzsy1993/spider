# -*- coding:utf-8 -*-
from selenium import webdriver
from lxml import etree
import requests
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
import  re,json
with open('result.json','rb') as fil:
    response=json.loads(fil.read())
    for i in response['dataInfo']['info']:
        print i['blockName']