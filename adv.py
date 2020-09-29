from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

def wonderer(player, world, room_graph):
	path = []  # visited paths
	room_stack = []  # visited rooms
	room_stack.append(player.current_room.id)  # add starting room to stack by id (should be 0)
	visited_rooms = set()

	# Big hint in the test written below: 'if len(visited_rooms) == len(room_graph)' we end the loop/test passes!
	while len(visited_rooms) != len(room_graph):
		current_room = room_stack[-1]  # current room will always be top item on stack
		visited_rooms.add(current_room)  # add current room to visited rooms
		connecting_rooms = room_graph[current_room][1]  # check main_maze for object clarity
		connecting_rooms_queue = []
		#print(current_room)
		
		for name, connected_room in connecting_rooms.items():  # checks keys with values
			if connected_room not in visited_rooms:  # have we been to the connected rooms?
				connecting_rooms_queue.append(connected_room)  # if not, add it to the queue

		# If there is a queue, set the first item to next_room
		if len(connecting_rooms_queue) != 0:
			next_room = connecting_rooms_queue[0]  # sets first item in queue to next_room
			room_stack.append(next_room)  # adds it to the stack

		# If the queue is empty
		else:
			room_stack.pop()  # get rid of last item on room_stack
			next_room = room_stack[-1]  # set the next_room to last item on room_stack
		for name, connected_room in connecting_rooms.items():  # for each name and connected_room in connecting_rooms
			if connected_room == next_room:   # if next_room is in connecting_rooms
				path.append(name)       # add the name of that room to the path
	return path


traversal_path = wonderer(player, world, room_graph)



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
"""
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
"""