from variables_domains import Slot, variables

def no_more_than_three_successive(variables: list):
    # Group slots by group
    slots_by_group = {}
    for var in variables:
        if var.slot is not None:
            if var.slot.day not in slots_by_group:
                slots_by_group[var.slot.day] = {}
            if var.group not in slots_by_group[var.slot.day]:
                slots_by_group[var.slot.day][var.group] = []
            slots_by_group[var.slot.day][var.group].append(var.slot.time)
    
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

print(no_more_than_three_successive([variables[22],variables[3],variables[4],variables[1]]))
# False car 


# from same group in the same day , it should return False
variables[1].slot = Slot(day='Sunday', time=1) 
variables[2].slot = Slot(day='Sunday', time=2)
variables[3].slot = Slot(day='Sunday', time=3) 
variables[4].slot = Slot(day='Sunday', time=4)

print(no_more_than_three_successive([variables[1],variables[2],variables[3],variables[4]]))