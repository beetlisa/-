class AccessCounter:
    def __init__(self):
        self.count = 0

    def __get__(self, instance, owner):
        self.count += 1
        return self.count