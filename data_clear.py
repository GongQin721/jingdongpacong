#coding:utf-8
# import xlrd
# datamsp = xlrd.open_workbook("ssd.xls")
import pandas as pd
datamsp = pd.read_excel('ssd.xls',dtype=str)
data =datamsp[['raw_title','view_price','item_loc','view_sales']]
data.head()

data['province'] = data.item_loc.apply(lambda  x:x.split()[0])
data['city'] = data.item_loc.apply(lambda  x:x.split()[0] if len(x)<4 else x.split()[1])

# def dealSales(x):
#     x = x.split('人')[0]
#     if '万' in x:
#         if '.' in x:
#             x = x.replace('.','').replace('万','0000')
#         else:
#             x =x.replace('万','0000')
#     return x.replace('+','')
# data['sales'] = data.view_sales.apply(lambda  x:dealSales(x))
data['sales'] = data.view_sales.apply(lambda  x:x.split('人')[0])
data['sales'] =data.sales.astype('int')

list_loc = ['province','city']
for i in list_loc:
    data[i] = data[i].astype('category')

data = data.drop(['item_loc','view_sales'],axis=1)

title = data.raw_title.values.tolist()
import jieba
title_s = []
for line in title:
    title_cut = jieba.lcut(line)
    title_s.append(title_cut)

stopwords = [line.strip() for line in open('ChineseStopWords.txt','r',encoding = 'ISO-8859-1').readlines()] #改变编码方式
#剔除停用词
title_clean = []
for line in title_s:
    line_clean = []
    for word in line:
        if word not in stopwords:
            line_clean.append(word)
    title_clean.append(line_clean)

title_clean_dist = []
for line in title_clean:
    line_dist = []
    for word in line:
        if word not in line_dist:
            line_dist.append(word)
    title_clean_dist.append(line_dist)


allwords_clean_dist = []
for line in title_clean_dist:
    for word in line:
        allwords_clean_dist.append(word)


df_allwords_clean_dist = pd.DataFrame({
    'allwords': allwords_clean_dist
})


word_count = df_allwords_clean_dist.allwords.value_counts().reset_index()
word_count.columns = ['word', 'count']


