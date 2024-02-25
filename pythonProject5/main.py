from PIL import Image
from PIL import ImageFilter

with (Image.open('Image.png') as pic_original):
    pic_original.show()

    pic_gray = pic_original.convert('L')
    pic_gray.save('Image1.png')
    pic_gray.show()

    pic_up = pic_gray.transpose(Image.ROTATE_90)
    pic_up.save('Image2.png')
    pic_up.show()

    pic_mirror = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirror.save('Image3.png')
    pic_mirror.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('Image4.png')
    pic_blured.show()