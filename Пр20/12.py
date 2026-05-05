class Age:
    def __set__(self, instance, value):
        if not (0 <= value <= 120):
            raise ValueError("Invalid age")
        instance.__dict__["value"] = value