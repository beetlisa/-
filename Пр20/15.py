class LogChange:
    def __set__(self, instance, value):
        old = instance.__dict__.get("value")
        print(f"{old} -> {value}")
        instance.__dict__["value"] = value