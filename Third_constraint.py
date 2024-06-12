from variables_domains import Slot, days, slots_per_day, CourseSession , all_slots , groups , courses , variables



def no_same_slot_different_courses(args):
    """
    we are going to check if the same slot is not allocated to different courses for the same group
    """
    # Do NOT INCLUDE SAME OBJECTS AS INPUTS BRUH
    # Create a dictionary to track groups and their allocated slots
    group_slots = {}
    
    
    for arg in args:
        
        # Check if the group's slot is already in the dictionary
        if arg.group in group_slots:
            if arg.slot in group_slots[arg.group]:
                # If the slot is already allocated to another course for the same group, return False
                return False
            else:
                # Otherwise, record the slot for the group
                group_slots[arg.group].append(arg.slot)
        else:
            # Initialize the group's slots list
            group_slots[arg.group] = [arg.slot]
                
    return True


# test the function

variables[0].slot = Slot(day='Sunday', time=1)
variables[1].slot = Slot(day='Sunday', time=2)

print(no_same_slot_different_courses([variables[0],variables[1]])) # True


variables[0].slot = Slot(day='Sunday', time=1)
variables[1].slot = Slot(day='Sunday', time=1)

print(no_same_slot_different_courses([variables[0],variables[1]])) # False