class base_cls:
        @staticmethod
        def register(cls, name):
                def f(ref):
                        cls._registry[name] = ref
                        return cls
                return f

class acquisition_cls (base_cls):
        def __init__(self, **kwargs):
                raise NotImplementedError()
        def acquire(self):
                raise NotImplementedError()
        def iterable(self):
                return False
        _registry = {}
        @classmethod
        def register(cls, name):
                return base_cls.register(cls, name)

class processing_cls (base_cls):
        _registry = {}
        def __init__(self, **kwargs):
                raise NotImplementedError()
        def process(self, img):
                raise NotImplementedError()
        _registry = {}
        @classmethod
        def register(cls, name):
                return base_cls.register(cls, name)

__all__ = ['acquisition_cls', 'processing_cls']
