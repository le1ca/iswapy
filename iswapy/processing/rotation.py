from base_classes import processing_cls
import skimage.transform

@processing_cls.register("rotation")
class rotation (processing_cls):

        def __init__(self, amount=0):
                self._amount = amount
                
        def process(self, img):
                img = skimage.transform.rotate(img, self._amount, True)
                print("Rotated %d degrees" % self._amount)
                return [img]
