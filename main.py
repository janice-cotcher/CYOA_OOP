class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

class Exit(object):
    def __init__(self, name, description):
        self.name = name
      
        self.description = description
        self.paths = {}
      
    def go(self, direction):
        return self.paths.get(direction, None)
      
    def add_paths(self, paths):
        self.paths.update(paths)
      
    def describe(self):
        return self.description

    def __str__(self):  
  
        return self.name

    def __repr__(self):
      
        return self.name

class RoomManager(object):
    def __init__(self):  
  
        self.rooms = {}
      
    def add_room(self, name, description):
        if name in self.rooms:
            raise ValueError('Room with name %s already exists' % name)            
        self.rooms[name] = Room(name, description)
      
    def add_exit(self, name, description):
        self.rooms[name] = Exit(name, description)
      
    def get_room(self, name):
        return self.rooms[name]
      
    def get_exit(self, name):
        return self.rooms[name]
      
    def get_rooms(self):
        return self.rooms.values()
      
    def get_exits(self):
        return self.rooms.values()
      
    def get_room_names(self):
        return self.rooms.keys()
      
    def get_exit_names(self):
        return self.rooms.keys()
      
    def get_room_description(self, name):
        return self.rooms[name].description
      
    def get_exit_description(self, name):
        return self.rooms[name].description
      
    def get_room_name(self, name):
        return self.rooms[name].name
      
    def get_exit_name(self, name):
        return self.rooms[name].name
      
    def get_room_paths(self, name):
        return self.rooms[name].paths
      
    def get_exit_paths(self, name):
        return self.rooms[name].paths
      
    def get_room_path(self, name, direction):
        return self.rooms[name].paths.get(direction, None)


class GameManager(object):
    def __init__(self):  
  
        self.rooms = RoomManager()
        self.exits = RoomManager()
      
    def add_room(self, name, description):
        self.rooms.add_room(name, description)
      
    def add_exit(self, name, description):
        self.exits.add_exit(name, description)
      
    def get_room(self, name):
        return self.rooms.get_room(name)
      
    def get_exit(self, name):
        return self.exits.get_exit(name)
      
    def get_rooms(self):
        return self.rooms.get_rooms()
      
    def get_exits(self):
        return self.exits.get_exits()
      
    def get_room_names(self):
        return self.rooms.get_room_names()
      
    def get_exit_names(self):
        return self.exits.get_exit_names()
      
    def get_room_description(self, name):
        return self.rooms.get_room_description(name)
      
    def get_exit_description(self, name):
        return self.exits.get_exit_description(name)
      
    def get_room_name(self, name):
        return self.rooms.get_room_name(name)
      
    def get_exit_name(self, name):
        return self.exits.get_exit_name(name)
      
    def get_room_paths(self, name):
        return self.rooms.get_room_paths(name)
      
    def get_exit_paths(self, name):
        return self.exits.get_exit_paths(name)
      
    def get_room_path(self, name, direction):
        return self.rooms.get_room_path(name, direction)
      
    def get_exit_path(self, name, direction):
        return self.exits.get_exit_path(name, direction)
      
   

class Player(object):
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
      
        self.exits = exits
      
    def get_name(self):
        return self.name
      
    def get_description(self):
        return self.description
        
    def get_exits(self):
        return self.exits
      
    def get_exit_paths(self, name):
        return self.exits.get_exit_paths(name)
      
    def get_exit_path(self, name, direction):
        return self.exits.get_exit_path(name, direction)
      
    def get_exit_description(self, name):
        return self.exits.get_exit_description(name)
      
    def get_exit_name(self, name):
        return self.exits.get_exit_name(name)
      

while True:
    print("Welcome to the game of Pathfinding!")
    print("Please enter the name of the room you want to enter:")
    room_name = input()
    print("Please enter the name of the exit you want to go through:")
    exit_name = input()
    print("Please enter the direction you want to go:")
    direction = input()
    print("Please enter the name of the room you want to go to:")
    destination_room_name = input()
    player = Player(room_name, room_name, Exit(exit_name, exit_name))
  
    print("You are in room: " + room_name)
  
    print("You are going to the exit: " + exit_name)
  
    print("You are going to the room: " + destination_room_name)
  
    print("You are going in the direction: " + direction)
  
    print("You are in the room: " + player.get_name())
      