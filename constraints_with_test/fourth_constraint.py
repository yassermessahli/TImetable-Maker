from variables_domains import Slot, days, slots_per_day, CourseSession , all_slots , groups , courses , variables



def no_same_slot_different_groups_same_td(variables: list):
    """
    we are going to check if the same slot is not allocated to different groups for the same td course
    """
    # Create a dictionary to track slots and their assigned courses for "td" and "tp" session types
    td_slots = {}

    for var in variables:
            if var.session_type in ["td" , 'tp']:
                # If the slot already has an assignment for "td" or "tp", check if it's from a different course
                if var.slot in td_slots:
                    if var.teacher in td_slots[var.slot] :
                        return False
                    else :
                         td_slots[var.slot].append(var.teacher)
                else:
                    # Otherwise, record the assignment
                    td_slots[var.slot] = [var.teacher]

    return True


#test the function
print(variables[1])
print(variables[22])

variables[1].slot = Slot(day='Sunday', time=1)
variables[22].slot = Slot(day='Sunday', time=1)

print(no_same_slot_different_groups_same_td([variables[1],variables[22]])) 