from variables_domains import Slot, days, slots_per_day, CourseSession , all_slots , groups , courses , variables

def no_same_slot_lectures(*args):
    """
    Lectures of the different courses should not be in the same slot
    """
    # Create a dictionary to track slots and the lectures assigned to them
    slot_lectures = {}
    
    for arg in args:
        # Only consider lecture sessions
        if arg.session_type == "lecture":
            if arg.slot in slot_lectures:
                # If the slot already has a lecture, check if it's from a different course
                if slot_lectures[arg.slot] != arg.course:
                    return False
            else:
                # Otherwise, record the lecture in the slot
                slot_lectures[arg.slot] = arg.course
                
    return True


#test the function
variables[2].slot = Slot(day='Sunday', time=2)
variables[0].slot = Slot(day='Sunday', time=1)

print(no_same_slot_lectures(variables[0],variables[2])) # True

variables[2].slot = Slot(day='Sunday', time=2)
variables[0].slot = Slot(day='Sunday', time=2)

print(no_same_slot_lectures(variables[0],variables[2])) # False