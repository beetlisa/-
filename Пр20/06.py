class Positive:
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Must be positive")
        instance.__dict__["value"] = value
