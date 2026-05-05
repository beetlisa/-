class Round2:
    def __set__(self, instance, value):
        instance.__dict__["value"] = round(value, 2)