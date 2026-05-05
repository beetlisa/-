class WriteOnce:
    def __set__(self, instance, value):
        if "value" in instance.__dict__:
            raise AttributeError("Already set")
        instance.__dict__["value"] = value