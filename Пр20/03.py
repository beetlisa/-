class LoggingSet:
    def __set__(self, instance, value):
        print("Setting value")
        instance.__dict__["value"] = value