class SafeFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
            return self.file
        except Exception as e:
            print("Error:", e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.file.close()
        except:
            pass
        print("File closed")

with SafeFile("input.txt") as f:
    if f:
        print(f.read())