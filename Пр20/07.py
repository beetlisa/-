class StringOnly:
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError
        instance.__dict__["value"] = value