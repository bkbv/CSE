class Room(object):
    def __init__(self, name, NORTH, WEST, SOUTH):
        # Things a Room has
        self.name = name
        self.north = NORTH
        self.west = WEST
        self.south = SOUTH

    def move(self, short_directions):
        global current_node
        current_node = globals()[getattr(self, short_directions)]

# Initialize Rooms
start = Room("You are west of house", None, )

west_house = Room("West of House", "north house", None)

while True:
    print(current_node['NAME'])
    print(current_node[''])
    command = input('>_')
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions
    if command in directions:
        try:


        except KeyError:
            print("You can not go this way")
    else:
        print('command not recongnized  ')
