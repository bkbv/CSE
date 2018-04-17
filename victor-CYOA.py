class Items(object):
    def __init__(self, name, color, material):
        self.name = name
        self.color = color
        self.material = material


class Clothing(Items):
    def __init__(self, name, color, material):
            super(Clothing, self).__init__(name, color, material)


class Outfit(Clothing):
    def __init__(self, name, color, material):
        super(Outfit, self).__init__(name, color, material)
        self.name = name
        self.color = color
        self.material = material

    def wear(self):
        print("You are wearing clothes")


class Shirt(Outfit):
    def __init__(self):
        super(Shirt, self).__init__("Jordan", "green", "dry_fit")

    def shirt_use(self):
        print("You are wearing a green jordan shirt")


class 
