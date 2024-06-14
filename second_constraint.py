from variables_domains import Slot, variables

def no_same_slot_lectures(variables: list):
    """
    Lectures of the different courses should not be in the same slot
    """
    # Create a dictionary to track slots and the lectures assigned to them
    slot_lectures = {}
    for var in variables:
        # Only consider lecture sessions
        if var.session_type == "lecture":
            if var.slot in slot_lectures:
                # If the slot already has a lecture, check if it's from a different course
                if slot_lectures[var.slot] != var.course:
                    return False
            else:
                # Otherwise, record the lecture in the slot
                slot_lectures[var.slot] = var.course
                
    return True


#test the function
variables[2].slot = Slot(day='Sunday', time=2)
variables[0].slot = Slot(day='Sunday', time=1)

print(no_same_slot_lectures([variables[0],variables[2]])) # True

variables[2].slot = Slot(day='Sunday', time=2)
variables[0].slot = Slot(day='Sunday', time=2)

print(no_same_slot_lectures([variables[0],variables[2]])) # False