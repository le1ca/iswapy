from base_classes import processing_cls

@processing_cls.register("split_frames")
class split_frames (processing_cls):

        def __init__(self):
                pass
                
        def process(self, img):
                return [img]
