#name:gq
#coding:utf-8

import re
import requests
import time


def getNowTime(form='%Y-%m-%d_%H-%M-%S'):
    nowTime = time.strftime(form, time.localtime())
    return nowTime

# 搜索关键字
searchKey = 'SSD'
# 输出文件编码（一般是utf-8，不过我用excel打开输出的csv文件发现会乱码，就用了ansi）
encode = 'ansi'
# keys是我要获取的宝贝信息属性
# keys = ('raw_title','view_price','item_loc','view_sales','comment_count','nick')
keys = ('raw_title','view_price','item_loc','view_sales','comment_count','nick')
url = 'https://s.taobao.com/search'
params = {'q':searchKey, 'ie':'utf8'}
header = {

    "cookie":"miid=140492274329679571; cna=4SazFX1DyxUCAbaKuaTl6ajR; t=fd451dec96bc937efd091929170750f9; cookie2=157f623c945eb7e5486575aa74bb82c3; _tb_token_=e8937869ee71e; v=0; uc3=nk2=2ieIephIBU8%3D&lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dByuWn8ICsW0Cj4jA%3D&id2=UoH3%2Bx439U1XcQ%3D%3D; csg=7c4fe0a6; lgc=%5Cu9F9A%5Cu74341993; dnk=%5Cu9F9A%5Cu74341993; skt=f1ce811104bfcd8d; existShop=MTU3MzQ0MzY2OA%3D%3D; uc4=id4=0%40UOnohDeT2YpJLW%2Bn445IdSv2uETC&nk4=0%402B2QzldysAw6sbH9Hpuyp4kzCQ%3D%3D; tracknick=%5Cu9F9A%5Cu74341993; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; enc=Ht0H%2BLDs0i1G%2BvlVSJL%2BI3wzMAdNiXg0nQ6uQALLdLZnUCCwos%2F76TF%2FJumLJD2ejAb%2BGbnzB14ZKE3PBpcXOw%3D%3D; mt=ci=-1_1; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hmAlh1iTw4WTZGH9xzCRsWZFu5Y5l4zAQg3umY05jj5nBqXVUdA75XDwRXpDO8Dus8SRS5oo%2BdRPcjgeKJOq6u7B7cd2G%2B2CYsyM564vqIiREEb9CdG%2BPTC4z1j8It8JN1ga6OsGzsFC3f3rRRHz4RXWFT70NM7kcj9Ors96w7zpNfds06k7c3d9sDE1%2B7VyjE1hh8WGjkVVWQaf7VPVAU%2Bn%2BTKPKO4p7%2BWrJbeexjulrtQdfmsTUQRQeKxjw%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; uc1=cookie14=UoTbnrygz3rySQ%3D%3D&cookie15=URm48syIIVrSKA%3D%3D; JSESSIONID=AA2AAADB72F82EC3DB9A094D093C2688; isg=BNPTDNIMijMlE0asQb1Nf48FYldRmCco6-t8E4XwVvIzBPKmA1gfmj4WPjTPpL9C; l=dBrEyui7qKn9qHKtBOCwVQKbM-bTMIRfguSJGwvXi_5Ce_Y16zbOkCTB3Ev6cjWAGLYD4aVvW6ytEeK_JsuKHdGJ4AadZxDDB",
    "referer":"https://s.taobao.com/search?q=%E9%9B%B6%E9%A3%9F&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191111&ie=utf8",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
startPage = 1 # 起始页面
pageTotal = 200# 爬取多少页
waitTime = 2 # 等待时间（如果爬的速度太快可能会出事）
rowWrited = 0
startTime = time.time()
print('任务启动\n{} | 初始化存储文件...'.format(getNowTime()))
fileName = r'tb_{}_{}_{}_{}.csv'.format(searchKey, startPage, pageTotal, getNowTime())
with open(fileName, 'w', encoding=encode) as saveFile:
    saveFile.write(','.join(keys) + '\n')

print('关键词:{} 起始页面:{} 爬取页面数:{}, 开始执行..'.format(searchKey, startPage, pageTotal))
for page in range(startPage, pageTotal+1):
    print('\npage{}: 获取数据...'.format(page))
    time.sleep(waitTime)
    params['s'] = str(page * 44) if page > 1 else '1'
    resp = requests.get(url, params, headers=header)
    results = [re.findall(r'"{}":"([^"]+)"'.format(key), resp.text.replace('\n','').replace('\r','').replace(',','').strip(), re.I) for key in keys]
    print('page{}: 正在写入数据...'.format(page))
    with open(fileName, 'a', encoding=encode) as saveFile:
        for row in range(len(results[0])):
            print('\r写入第{}条..'.format(row+1), end='')
            rowWrited += 1
            for key in range(len(results)):
                try:
                    saveFile.write('{}{}'.format(results[key][row], ',' if key+1<len(results) else '\n'))
                except:
                    saveFile.write('null{}'.format(',' if key+1<len(results) else '\n'))
    print('page{}完成...'.format(page, len(results[0])))

print('\n任务完成!! 页面总数: {} | 写入数据: {}条 | 用时: {:.2f}s'.format(pageTotal, rowWrited, time.time()-startTime))


