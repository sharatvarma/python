'''
Created on Sep 1, 2016

@author: murthyraju
'''


class Pixel(object):
    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def reddify(self, red_increment):
        self.red = self.red + red_increment

    def __str__(self):
        #return str(self.red) + "-" + str(self.green) + "-" + str(self.blue) + "-" + str(self.alpha)
        return "%s-%s-%s-%s" % (self.red, self.green, self.blue, self.alpha) # formatting operator


class Row(object):
    def __init__(self, pixels):
        self.pixels = pixels

    def __str__(self):
        row_string = ""
        for pixel in self.pixels:
            #print(type(pixel))
            row_string += " " + pixel.__str__()
        return row_string


class Image(object):
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        image_string = ""
        for row in self.rows:
            image_string = image_string + "\n" + row.__str__()
        return image_string

pixel1_1 = Pixel(0, 0, 0, 0)
pixel1_2 = Pixel(0, 0, 0, 0)
pixel1_3 = Pixel(0, 0, 0, 0)
pixel1_4 = Pixel(0, 0, 0, 0)
pixel1_5 = Pixel(0, 0, 0, 0)

pixel2_1 = Pixel(0, 0, 0, 0)
pixel2_2 = Pixel(0, 0, 0, 0)
pixel2_3 = Pixel(0, 0, 0, 0)
pixel2_4 = Pixel(0, 0, 0, 0)
pixel2_5 = Pixel(0, 0, 0, 0)

row1 = Row([pixel1_1, pixel1_2, pixel1_3, pixel1_4, pixel1_5])
row2 = Row([pixel2_1, pixel2_2, pixel2_3, pixel2_4, pixel2_5])

image1 = Image([row1, row2])

image1.rows[0].pixels[0].reddify(100)

print image1
