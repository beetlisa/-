class LoggingGet:
    def __get__(self, instance, owner):
        print("Getting value")
        return instance.__dict__.get("value")