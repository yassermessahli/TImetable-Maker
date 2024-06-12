from variables_domains import Slot, days, slots_per_day, CourseSession , all_slots , groups , courses , variables



def no_same_slot_different_groups_same_td(*args):
    """
    we are going to check if the same slot is not allocated to different groups for the same td course
    """
    # Create a dictionary to track slots and their assigned courses for "td" and "tp" session types
    td_slots = {}

    for arg in args:
            if arg.session_type == "td":
                # If the slot already has an assignment for "td" or "tp", check if it's from a different course
                if arg.slot in td_slots:
                    if td_slots[arg.slot] == arg.course:
                        return False
                else:
                    # Otherwise, record the assignment
                    td_slots[arg.slot] = arg.course

    return True


#test the function
print(variables[1])
print(variables[22])

variables[1].slot = Slot(day='Sunday', time=1)
variables[22].slot = Slot(day='Sunday', time=1)

print(no_same_slot_different_groups_same_td(variables[1],variables[22])) # False