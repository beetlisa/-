class Cached:
    def __get__(self, instance, owner):
        if "value" not in instance.__dict__:
            instance.__dict__["value"] = 42  # вычисление
        return instance.__dict__["value"]