class Book:
    __slots__ = ('title', 'author')

    def info(self):
        print(self.title, "-", self.author)

b = Book()
b.title = "1984"
b.author = "Orwell"
b.info()
