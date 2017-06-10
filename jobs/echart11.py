# -*- coding: utf-8 -*-
import json
from collections import Counter
with open('jobs.json') as f:
    data=json.loads(f.read().encode('utf-8'))
title={}
pos_num=0
for pos in data:
    t=pos['title']
    try:
        n=int(pos['num'])
    except:
        n=3
    title[t]=title.get(t,0)+n
    pos_num+=n
most_title=Counter(title).most_common(10)
# print(most_title)
# print(pos_num)
for item in most_title:
    print("'%s',"%item[0],end=''),
    # print("{name:'%s',value:%d},"% item)
    # pos_num -=item[1]
# print("{name:'其他',value:%d},"%pos_num)
