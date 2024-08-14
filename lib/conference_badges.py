def badge_maker(name):
    badge= f"Hello, my name is {name}."
    return badge

def batch_badge_creator(names):
    batch_names = []
    for name in names: 
        message = f"Hello, my name is {name}."
        batch_names.append(message)
    
    return batch_names

def assign_rooms(names):
    room_list= []
    for room, name in enumerate(names):
# enumerate() allows you to iterate over a sequence 
# and retrieve both the index and 
# the value of each element in the sequence.
        room_number = room+1
        message = f"Hello, {name}! You'll be assigned to room {room_number}!"
        room_list.append(message)
    return room_list

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    for badge in badges:
        print(badge)

    for room in room_assignments:
        print(room)


