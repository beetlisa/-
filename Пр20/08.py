class DefaultValue:
    def __get__(self, instance, owner):
        return instance.__dict__.get("value", "default")

    def __set__(self, instance, value):
        instance.__dict__["value"] = value