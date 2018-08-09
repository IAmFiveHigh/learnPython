from PIL import Image

# file 文件地址
file = './icon.jpeg'
# filename 文件生成名字
filename = 'icon'

# 1x图尺寸
oneXW, oneXH = (60, 60)

img = Image.open(file)
new2x = img.resize((oneXW * 2, oneXH * 2))
new2x.save(f'./{filename}@2x.png')

new3x = img.resize((oneXW * 3, oneXH * 3))
new3x.save(f'./{filename}@3x.png')

