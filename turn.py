# from PIL import Image, ImageFilter
 
# # 이미지 회전하기
# # img = Image.open(file)
# # img_new = img.transpose(method=Image.ROTATE_90) #90도 회전
# # img_new.save(file, quality=100)     # 회전한 파일 저장하기.

from PIL import Image, ImageFilter

import glob

images = glob.glob('file_path/*.jpg')
for fname in images :
    img = Image.open(fname)
    img_new = img.transpose(method=Image.ROTATE_180) #180도 회전
    img_new.save(fname, quality=100) #회전한 파일 저장