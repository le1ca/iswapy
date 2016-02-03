from base_classes import processing_cls
import skimage.transform

@processing_cls.register("scale")
class scale (processing_cls):

        def __init__(self, mode="keep-ratio", width=None, height=None):
                self._mode = mode
                self._width = width
                self._height = height
                
        def process(self, img):
                if self._mode == "keep-ratio":
                        y, x = img.shape
                        if self._width == None:
                                factor = 1.0 * y / self._height
                                height = self._height
                                width  = round(x / factor)
                        elif self._height == None:
                                factor = 1.0 * x / self._width
                                width = self._width
                                height = round(y / factor)
                        else:
                                raise ValueError("keep-ratio mode needs either height or width to be specified")
                else:
                        raise ValueError("unknown scale mode %s" % self._mode)
                img = skimage.transform.resize(img, (height, width) )
                print("Scaled to %dx%d" % (width, height))
                return [img]
