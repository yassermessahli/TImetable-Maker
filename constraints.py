from variables_domains import Slot, variables

def no_more_than_three_successive(variables: list):
    # Group slots by group
    slots_by_group = {}
    for var in variables:
        # if the variable is note assigned a slot, skip it
        if var.slot is None:
            continue
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


def no_same_slot_lectures(variables: list):
    """
    Lectures of the different courses should not be in the same slot
    """
    # Create a dictionary to track slots and the lectures assigned to them
    slot_lectures = {}
    for var in variables:
        # if the variable is note assigned a slot, skip it
        if var.slot is None:
            continue
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


def no_same_slot_different_courses(variables: list):
    """
    check if the same slot is not allocated to different courses for the same group
    """
    # Do NOT INCLUDE SAME OBJECTS AS INPUTS BRUH
    # Create a dictionary to track groups and their allocated slots
    group_slots = {}
    for var in variables:
        # if the variable is note assigned a slot, skip it
        if var.slot is None:
            continue
        # Check if the group's slot is already in the dictionary
        if var.group in group_slots:
            if var.slot in group_slots[var.group]:
                # If the slot is already allocated to another course for the same group, return False
                return False
            else:
                # Otherwise, record the slot for the group
                group_slots[var.group].append(var.slot)
        else:
            # Initialize the group's slots list
            group_slots[var.group] = [var.slot]
    return True


def no_same_slot_different_groups_same_td(variables: list):
    """
    we are going to check if the same slot is not allocated to different groups for the same td course
    """
    # Create a dictionary to track slots and their assigned courses for "td" and "tp" session types
    td_slots = {}

    for var in variables:
        # if the variable is note assigned a slot, skip it
        if var.slot is None:
            continue
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


def same_slot_for_lectures_of_same_course(variables: list):
    """Ensure that lectures of the same course are in the same slots across all groups."""
    
    course_slots = {}
    for var in variables:
        # if the variable is note assigned a slot, skip it
        if var.slot is None:
            continue
        if var.session_type == "lecture":
            if var.course in course_slots:  
                if var.slot != course_slots[var.course]:
                    return False
            else:
                course_slots[var.course] = var.slot
    return True

def max_two_days_per_teacher(variables: list):
    # Create a dictionary to track the days each teacher is assigned
    teacher_days = {}

    for var in variables:
        # if the variable is note assigned a slot, skip it        
        if var.slot is None:
            continue
        
        # Get the teacher of the current CourseSession
        teacher = var.teacher
        if teacher in teacher_days:
            teacher_days[teacher].append(var.slot.day)
            # If the teacher already has two days assigned, return False
            if len(set(teacher_days[teacher])) > 2:
                return False
            
            # Otherwise, add the current day to the list of assigned days for the teacher
        else:
            # If the teacher has no assigned days, initialize the list with the current day
            teacher_days[teacher] = [var.slot.day]
        # print(teacher_days[teacher])
    return True