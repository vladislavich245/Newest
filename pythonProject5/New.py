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

MyImage = ImageEditor('Image.png')
MyImage.open()
MyImage.do_bw()