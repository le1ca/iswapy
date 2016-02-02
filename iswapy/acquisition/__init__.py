# import all modules in this directory
# borrowed from http://stackoverflow.com/questions/1057431/
import os, glob
modules = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]
__all__ = [f for f in modules if f != "__init__"]
for f in __all__:
        __import__("acquisition.%s" %f)
