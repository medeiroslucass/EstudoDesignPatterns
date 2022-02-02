

class MetaSingleton(type):

    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance

class Logger(metaclass=MetaSingleton):
    pass

log1 = Logger()
print(f'Log 1: {id(log1)}')

log2 = Logger()
print(f"Log 2: {id(log2)}")