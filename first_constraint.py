from variables_domains import Slot, days, slots_per_day, CourseSession , all_slots , groups , courses , variables

def no_more_than_three_successive(*args):
    # Extract the slots from the CourseSession objects
    slots = [arg.slot for arg in args]
    
    # Group slots by group
    slots_by_group = {}
    for arg in args:
        if arg.slot.day not in slots_by_group:
            slots_by_group[arg.slot.day] = {}
        if arg.group not in slots_by_group[arg.slot.day]:
            slots_by_group[arg.slot.day][arg.group] = []
        slots_by_group[arg.slot.day][arg.group].append(arg.slot.time)
    
    # Check each group's slots for each day
    for day, groups in slots_by_group.items():
        for group, group_slots in groups.items():
            group_slots.sort()
            for i in range(len(group_slots) - 3):
                if group_slots[i+3] - group_slots[i] <= 3:
                    return False
    return True



#test the function
# from different groups in the same day , it should return True
variables[1].slot = Slot(day='Sunday', time=1) 
variables[22].slot = Slot(day='Sunday', time=2)
variables[3].slot = Slot(day='Sunday', time=3) 
variables[4].slot = Slot(day='Sunday', time=4)

print(no_more_than_three_successive(variables[22],variables[3],variables[4],variables[1]))
# False car 


# from same group in the same day , it should return False
variables[1].slot = Slot(day='Sunday', time=1) 
variables[2].slot = Slot(day='Sunday', time=2)
variables[3].slot = Slot(day='Sunday', time=3) 
variables[4].slot = Slot(day='Sunday', time=4)

print(no_more_than_three_successive(variables[1],variables[2],variables[3],variables[4]))