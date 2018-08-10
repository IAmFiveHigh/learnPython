from PIL import Image

l = ["0元购机.png", "按月付租.png", "闪电发货.png", "正品.png"]
for f in l:
    # file 文件地址
    file = f'./{f}'
    # filename 文件生成名字
    filename = f.split('.')[0]

    # 1x图尺寸
    oneXW, oneXH = (60, 60)

    img = Image.open(file)
    new2x = img.resize((oneXW * 2, oneXH * 2))
    new2x.save(f'./{filename}@2x.png')

    new3x = img.resize((oneXW * 3, oneXH * 3))
    new3x.save(f'./{filename}@3x.png')


