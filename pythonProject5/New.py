from PIL import Image
from PIL import ImageFilter
class ImageEditor():
    def __init__(self,filename):
        self.filename = filename
        self.original = None
        self.changed = list()
    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не знайдено!')
        self.original.show()
    def do_bw(self):
        gray = self.original.convert('L')
        self.changed.append(gray)
        gray.save('gray.png')
    def do_up(self):
        up = self.original.transpose(Image.ROTATE_90)
        self.changed.append(up)
        up.save('up.png')
    def do_mir(self):
        mirr = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(mirr)
        mirr.save('mirr.png')
    def do_bl(self):
        gray = self.original.filter(ImageFilter.BLUR)
        self.changed.append(gray)
        gray.save('blur.png')


MyImage = ImageEditor('Image.png')
MyImage.open()
MyImage.do_bw()
MyImage.do_up()
MyImage.do_mir()
MyImage.do_bl()
