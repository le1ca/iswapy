from base_classes import processing_cls
import skimage.util

@processing_cls.register("split_frames")
class split_frames (processing_cls):

        def __init__(self, width, space, buffer=0):
                self._w = width
                self._s = space
                self._b = buffer
                
        def process(self, img):
                ret = []
                accum = 0
                _, w = img.shape
                while accum + self._w < w:
                        ret.append(skimage.util.crop(img, ((0, 0), (accum, w - (accum + self._w + self._b/2)))))
                        print("Split frame %d pixels wide." % self._w)
                        accum += self._w + self._s - self._b/2
                return ret
