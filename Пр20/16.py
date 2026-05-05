class Linked:
    def __set__(self, instance, value):
        instance.__dict__["a"] = value
        instance.__dict__["b"] = value * 2