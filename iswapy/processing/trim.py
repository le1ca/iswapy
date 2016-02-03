from base_classes import processing_cls
import skimage.util

@processing_cls.register("trim")
class trim (processing_cls):

        def __init__(self, top=0, bottom=0, left=0, right=0):
                self._top = top
                self._bottom = bottom
                self._left = left
                self._right = right
                
        def process(self, img):
                img = skimage.util.crop(img, ((self._top, self._bottom), (self._left, self._right)))
                print("Cropped image.")
                return [img]
