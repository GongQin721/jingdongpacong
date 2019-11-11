# coding:utf-8

import os
import time
import json
import random
import requests

COMMENT_FILE_PATH = 'jd_an3+_comment.txt'

def spider_comment(page=0):
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2736&productId=100001845588'\
          '&score=0&sortType=6&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1'%page
    kv = {'user-agent': 'Mozilla/5.0', 'Referer': 'https://item.jd.com/100001845588.html'}

    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
    except:
        print('scrapy fail')

    r_json_str = r.text[26:-2]

    r_json_obj = json.loads(r_json_str)

    r_json_comments = r_json_obj['comments']

    for r_json_comment in r_json_comments:

        with open(COMMENT_FILE_PATH, 'a') as file:
            file.write(r_json_comment['content'] + '\n')

    file.close()


def batch_spider_comment():

    if os.path.exists(COMMENT_FILE_PATH):
        os.remove(COMMENT_FILE_PATH)
    for i in range(100):
        spider_comment(i)
        time.sleep(random.random() * 5)

if __name__ == '__main__':
    batch_spider_comment()





