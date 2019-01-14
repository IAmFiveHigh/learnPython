"""
  created by IAmFiveHigh on 2019-01-13
 """
import requests
import re
import numpy as np
import time
import json

# small_comment_image_url = 'img30.360buyimg.com/n0/s48x48_jfs/t26500/343/1741452158/221453/329361d1/5becbae5Nb904e1b4.jpg'
# big_comment_image_url = 'img30.360buyimg.com/shaidan/s616x405_jfs/t26500/343/1741452158/221453/329361d1/5becbae5Nb904e1b4.jpg'

# app上线时间
app_up_time = int(time.mktime(time.strptime('2018-12-15 00:00:00', '%Y-%m-%d %H:%M:%S')))

# 上传图片地址
up_load_url = 'http://xx.xx.xxx.xx/xxxxxx/fileupload'
up_header = {"content-type":"multipart/form-data"}

kv = {'user-agent':'mozilla/5.0'}

skus = [
    '100001165254',
    '33743197985',
    '100001860767',
    '100000177748',
    '1892019',
    '100000206154',
    '4325427',
    '6805332',
    '7629588',
    '7842695'
    ]


def exchange_comment(comment_item):
    comment_item = re.sub('京东物流', '', comment_item)
    comment_item = re.sub('狗东|京东|二手东|jd|JD|Jd|jD|jingdong', '麦粒儿', comment_item)
    comment_item = re.sub('自营', '', comment_item)
    comment_item = re.sub('买', '租', comment_item)
    comment_item = re.sub('\n', '', comment_item)
    return comment_item


def upload_image(images_array):
    if len(images_array) == 0:
        return ''
    data = {}
    for i in images_array:
        time.sleep(0.1)
        r = requests.get(i, headers=kv)
        img_name = re.search('([a-zA-Z0-9]+\.jpg)', i).group()
        data[img_name] = r.content

    r = requests.post(up_load_url, files=data)
    response = json.loads(r.text)
    return ";".join(response['url'])


for sku in skus:
    product_name = ''
    product_comment_array = []

    for i in range(10):
        time.sleep(1)
        comment_url = f'http://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv0&productId={sku}&score=0&sortType=5&page={i}&pageSize=10&isShadowSku={sku}&rid=0&fold=1'
        r = requests.get(comment_url)
        json_str = r.text

        json_str = re.sub('fetchJSON_comment98[0-9a-zA-Z]+\(', '', json_str)
        json_str = re.sub('\);', '', json_str)
        json_data = json.loads(json_str)
        comment = json_data['comments']
        for j in comment:

            product_name = j['referenceName'].strip()[0:20]
            # 评论内容 如果为此用户未填写评价内容 则跳过
            content = exchange_comment(j['content'])
            if content == '此用户未填写评价内容':
                continue

            # 评价星级
            score = j['score']
            if score < 5:
                continue

            # 评论人昵称
            name = j['nickname']
            # 评论时间
            creation_time = j['creationTime']

            # 判断时间是否过早
            t1 = int(time.mktime(time.strptime(creation_time, '%Y-%m-%d %H:%M:%S')))
            if t1 < app_up_time:
                continue

            print(score, name, creation_time, content)

            # image
            if 'images' in j.keys():

                images = j['images']
                images_array = []
                for k in images:
                    img_url = k['imgUrl']
                    img_url = re.sub('n0/s[0-9]{2,3}x[0-9]{2,3}_jfs', 'shaidan/s616x405_jfs', img_url)
                    img_url = 'http:' + img_url
                    images_array.append(img_url)
                product_comment_array.append([score, name, content, creation_time, upload_image(images_array)])


    product_np = np.array(product_comment_array)
    np.savetxt(f'{product_name}.csv', product_np, fmt='%s', delimiter=',')

