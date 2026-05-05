class MaxLength:
    def __set__(self, instance, value):
        if len(value) > 10:
            raise ValueError("Too long")
        instance.__dict__["value"] = value