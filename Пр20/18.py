class NumberList:
    def __set__(self, instance, value):
        if not all(isinstance(x, (int, float)) for x in value):
            raise TypeError
        instance.__dict__["value"] = value