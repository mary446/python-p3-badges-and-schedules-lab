def badge_maker(name = "Yna"):
    return f"Hello, my name is {name}."

def batch_badge_creator(names = "Yna , Arel"):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms= range(1, 7)
    assignment = []
    for room in rooms:
        assignment.append(f"Hello, {names[room - 1]}! You'll be assigned to room {room}!")
    return assignment

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for assignment in assign_rooms(names):
        print (assignment)
