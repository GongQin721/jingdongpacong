# encoding:utf-8
from bs4 import BeautifulSoup
import re,requests,json

totalPage=1000

s=requests.session()#会话对象
url='https://sclub.jd.com/comment/productPageComments.action'
 #要访问网页所需要的参数值
data={
    'callback':'fetchJSON_comment98vv214',#是网页响应采用的json格式，这个一般不相同也不会有太大问题
    'productId':'12272819',
    'score':0,
    'sortType':3,
    'page':0,
    'pageSize':10,
    'isShadowSku':0

}

def write_to_file(contents):
    
    with open('result.txt','a',encoding='utf-8') as f:
        
        for content in contents:
            
            f.write(json.dumps(content, ensure_ascii=False)+'\n')
            
            #json序列化默认使用ascii编码，这里禁用ascii
        f.close()

def getData(j):
    commentSummary=j['comments']
    
    for comment in commentSummary:#对结果进行迭代
        ##遍历列表，用一个生成器来存储遍历到的结果，重新编写字典
       
        yield{
                'client_name':comment['nickname'],
                'date_comment':comment['referenceTime'],
                'comment':comment['content'],
                'client':comment['userClientShow']
              }#每次遇到yield关键字后返回相应结果，并保留函数当前的运行状态，等待下一次的调用。
        
        # print('{} {} {}\n{}\n'.format(c_name,c_time,c_client,c_content))

while True:
    t=s.get(url,params=data).text#回值t就是我们构建的评论网址的     内容
    #往这个URL地址传送data里面的数据，params是添加到url的请求字符串中的，用于get请求
    try:
        t=re.search('(?<=fetchJSON_comment98vv214\().*(?=\);)',t).group(0)
        #re.search()函数将对整个字符串进行搜索，并返回第一个匹配的字符串的match对象，匹配到的整个字符串/整个正则匹配的内容
    except Exception as e:
        break
    j=json.loads(t)
    ##将爬取下来的内容转化成可以被json解析的字典格式
    infos=getData(j)
    write_to_file(infos)
    #每一次迭代，每一次中断，写入一次数据
    data['page']+=1
    if data['page']>=totalPage:
        break    



