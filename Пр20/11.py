class Email:
    def __set__(self, instance, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        instance.__dict__["value"] = value