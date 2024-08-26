# https://stackoverflow.com/questions/6760685/what-is-the-best-way-of-implementing-singleton-in-python

class Singleton(object):
    _instancia = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instancia, class_):
            class_._instancia = object.__new__(class_, *args, **kwargs)
        return class_._instancia