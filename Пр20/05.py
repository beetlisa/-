class IntOnly:
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Only int allowed")
        instance.__dict__["value"] = value