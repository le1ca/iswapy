from base_classes import processing_cls
import skimage.exposure

@processing_cls.register("sigmoidal_contrast")
class sigmoidal_contrast (processing_cls):

        def __init__(self, negative=False, cutoff=0.5, gain=10):
                self._neg = negative
                self._cutoff = cutoff
                self._gain = gain
                
        def process(self, img):
                img = skimage.exposure.adjust_sigmoid(img, cutoff=self._cutoff, gain=self._gain, inv=self._neg)
                print("Adjusted contrast.")
                return [img]
