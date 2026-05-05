class User:
    __slots__ = ('login', 'password')

    def change_password(self, new_password):
        self.password = new_password

u = User()
u.login = "admin"
u.password = "1234"

u.change_password("abcd")
print(u.password)
