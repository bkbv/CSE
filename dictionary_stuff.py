World_map = {
    'WESTHOUSE': {
        'NAME': "WEST OF HOUSE",
        "DESCRIPTION": "YOU ARE WEST OF HOUSE",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'SOUTH OF HOUSE',
        'DESCRIPTION': "INSERT DESCRIPTION HERE",
        'PATH': {
            'SOUTH': 'WESTGOUSE'
        }
    }
}
current_node = World_map['WESTHOUSE']
directions = ('NORTH', 'SOUTH', 'EAST', 'WEST')

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = World_map[name_of_node]
        except KeyError:
            print("You can not go this way")
    else:
        print('command not recongnized  ')