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

    def Wear(self):
        print("You are wearing clothes")


class Shirt(Outfit):
    def __init__(self):
        super(Shirt, self).__init__("Jordan", "green", "dry_fit")

    def shirt_use(self):
        print("You are wearing a green jordan shirt")


class Tools(Shirt):
    def __init__(self):
        super(Tools, self).__init__()

        class Room(object):
            def __init__(self, name, north, west, south):
                self.name = name
                self.north = north
                self.west = west
                self.south = south

            def move(self, direction):
                global current_node
                current_node = globals()[getattr(self, direction)]

# Initialize Rooms
Rm1 =("You are west of house", None)

west_house = Rm1("West of House", "north house", None)

while True:
            print(current_node.name)
            print(current_node.description)
            command = input('>_').lower().strip()
            if command == 'quit':
                quit(0)
            elif command in direction:
                # Look for which command we typed in
                pos = direction.index(command)
                # Change the command to be the long form
                command = direction[pos]
            if command in direction:
                try:
                    current_node.move(command)
                except KeyError:
                    print("You can not go this way")
            else:
                print('command not recongnized')
