import json, warnings
import acquisition, processing
from base_classes import *

class iswapy:
        def __init__(self, acqu, proc):
                self._acqu = iswapy.make_acquisition(acqu['module'], acqu['options'])
                self._proc = [
                        iswapy.make_processing(x['module'], x['options'])
                        for x in proc
                ]
        
        def go(self):
                imgs = self._acqu.acquire()
                for f in self._proc:
                        new = []
                        for im in imgs:
                                new.extend(f.process(im))
                        imgs = new
        
        def iterable(self):
                return self._acqu.iterable()
        
        @staticmethod
        def make_acquisition(module, options):
                return acquisition_cls._registry[str(module)](**options)
        
        @staticmethod
        def make_processing(module, options):
                return processing_cls._registry[str(module)](**options)
        
def main(args):
        cfg = json.load(open(args[1], 'r'))
        isw = iswapy(cfg['acquisition'], cfg['processing'])
        
        cont = True
        while cont:
                with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        isw.go()
                cont = isw.iterable()
