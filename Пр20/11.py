class Product:
    __slots__ = ('name', 'price')

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.price = value

p = Product()
p.name = "Phone"

p.set_price(500)
print(p.price)

try:
    p.set_price(-10)
except ValueError as e:
    print(e)
