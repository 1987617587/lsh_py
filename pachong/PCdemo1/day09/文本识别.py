import pytesseract
from PIL import Image

# 英文
# image = Image.open('./images/tesseracttest.jpg')
#
# text = pytesseract.image_to_string(image)
# print(text)
# # 中文
# image = Image.open('./images/hz.png')
#
# text = pytesseract.image_to_string(image)
# print(text)
# 文本带背景
image = Image.open('./images/recaptcha.png')
image.show()
# 灰度化处理
gray = image.convert('L')
gray.show()
# 二值化处理
threshold = 1
bw = gray.point(lambda x: 0 if x < threshold else 255, '1')
bw.show()
# 此时只有0和255，0的就是想要的信息
text = pytesseract.image_to_string(bw)
print(text)
