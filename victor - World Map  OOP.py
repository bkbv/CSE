class Room(object):
    def __init__(self, name, north, west, south):
        # Things a Room has
        self.name = name
        self.north = north
        self.west = west
        self.south = south

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

# Initialize Rooms 
Rm1 = Room("You are west of house", None)

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
