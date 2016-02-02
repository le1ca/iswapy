from base_classes import processing_cls
import skimage.io

@processing_cls.register("jpeg")
class jpeg (processing_cls):

        def __init__(self, name, quality=85):
                self._name  = str(name)
                self._count = 1
                
        def process(self, img):
                try:
                        name = self._name % self._count
                except ValueError:
                        name = self._name
                skimage.io.imsave(name, img)
                print("Saved '%s'." % name)
                self._count = self._count + 1
                return [img]
