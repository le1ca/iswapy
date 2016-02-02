import sys, re, skimage.io
from base_classes import acquisition_cls

@acquisition_cls.register("jpeg")
class jpeg (acquisition_cls):

        def __init__(self, name):
                m = re.match(r"^##argument(\d+)##$", name)
                if m != None:
                        name = sys.argv[int(m.group(1))]
                self._name = name
                
        def acquire(self):
                im = skimage.io.imread(self._name)
                print("Loaded '%s'." % self._name)
                return [im]
