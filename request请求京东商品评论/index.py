"""
  created by IAmFiveHigh on 2019-01-13
 """
import requests
import re
import numpy as np
import time
import json


# //img30.360buyimg.com/shaidan/s616x405_jfs/t1/731/3/13167/676032/5bd49c37Eb9b334f5/9cfd67bc17ce8eb9.jpg
# //img30.360buyimg.com/n0/s48x48_jfs/t1/731/3/13167/676032/5bd49c37Eb9b334f5/9cfd67bc17ce8eb9.jpg

small_comment_image_url = 'img30.360buyimg.com/n0/s48x48_jfs/t26500/343/1741452158/221453/329361d1/5becbae5Nb904e1b4.jpg'
big_comment_image_url = 'img30.360buyimg.com/shaidan/s616x405_jfs/t26500/343/1741452158/221453/329361d1/5becbae5Nb904e1b4.jpg'

# app上线时间
app_up_time = int(time.mktime(time.strptime('2018-12-15 00:00:00', '%Y-%m-%d %H:%M:%S')))

skus = [
    '100001165254',
    '33743197985'
    ]


def exchange_comment(comment_item):
    comment_item = re.sub('京东物流', '', comment_item)
    comment_item = re.sub('狗东|京东|二手东|jd|JD|Jd|jD|jingdong', '麦粒儿', comment_item)
    comment_item = re.sub('自营', '', comment_item)
    comment_item = re.sub('买', '租', comment_item)
    comment_item = re.sub('\n', '', comment_item)
    return comment_item


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

            # 评论人昵称
            name = j['nickname']
            # 评论时间
            creation_time = j['creationTime']

            # 判断时间是否过早
            t1 = int(time.mktime(time.strptime(creation_time, '%Y-%m-%d %H:%M:%S')))
            if t1 < app_up_time:
                continue

            print(name, creation_time, content)

            # image
            if 'images' in j.keys():

                images = j['images']
                images_array = []
                for k in images:
                    img_url = k['imgUrl']
                    img_url = re.sub('n0/s[0-9]{2,3}x[0-9]{2,3}_jfs', 'shaidan/s616x405_jfs', img_url)
                    img_url = 'http:' + img_url
                    images_array.append(img_url)
                images_url_array = ';'.join(images_array)
                product_comment_array.append([name, content, creation_time, images_url_array])


    product_np = np.array(product_comment_array)
    np.savetxt(f'{product_name}.csv', product_np, fmt='%s', delimiter=',')

