# -*- coding:utf-8 -*-
import re
str="http://hz.ziroom.com/z/vr/61318695.html"
print re.findall(r'\d+',str)[0]