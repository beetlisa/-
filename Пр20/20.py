class ComplexDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        print("Getting value")
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Must be int")
        if not (0 <= value <= 100):
            raise ValueError("Out of range")

        old = instance.__dict__.get(self.name)
        print(f"{old} -> {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete")