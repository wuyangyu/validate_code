#!/usr/bin/env python
# coding: utf-8

import random
import Image,ImageDraw,ImageFont
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO


class RandomChar():
    #生成ascii随机字符
    @staticmethod
    def ascii():
        v = []
        s = ""
        for x in range(0,4):
            v.append(chr(random.randint(0x21,0x7e)))
            s += " %s" % v[x]
        return s

class ImageChar():
    #生成image字符
    def __init__(self,fontColor = (0,0,0),
                 fontPath = "font.otf",
                 size=(200,40),
                 bgColor = (255,255,255),
                 fontSize = 30,rand_str = None):

        self.fontSize = fontSize
        self.fontColor = fontColor
        self.bgColor = bgColor
        self.fontPath = fontPath
        self.font = ImageFont.truetype(self.fontPath,self.fontSize)
        self.image = Image.new('RGB',size,self.bgColor)
        self.rand_str = rand_str

    def drawLine(self):
        draw = ImageDraw.Draw(self.image)
        draw.line((0, 0) + self.image.size, fill=128)
        draw.line((0,self.image.size[1],self.image.size[0],0),fill=128)
        del draw

    def drawText(self):
        draw = ImageDraw.Draw(self.image)
        draw.text((30,7),self.rand_str,font=self.font,fill = self.fontColor)
        del draw

    def show(self,name = "test"):
        self.drawText()
        self.drawLine()
        self.image.save(name,"GIF")

    def ShowStrIO(self):
        self.drawText()
        self.drawLine()
        stream = StringIO.StringIO()
        self.image.save(stream,"GIF")

if __name__ == "__main__":
    test = ImageChar(rand_str=RandomChar.ascii())
    test.show()


