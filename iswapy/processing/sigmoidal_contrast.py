from base_classes import processing_cls

@processing_cls.register("sigmoidal_contrast")
class sigmoidal_contrast (processing_cls):

        def __init__(self, negative=False, cutoff=0.5, gain=10):
                pass
                
        def process(self, img):
                return [img]
