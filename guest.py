class Party:
    def __init__(self, name, email,preference):
        self.name = name
        self.email = email
        self.preference = preference

x = Party("raya", "example@email.com", "vegan")
print(x.name)
print(x.preference)
print(x.email)


