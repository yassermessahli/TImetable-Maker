def same_slot_for_lectures_of_same_course(variables: list):
    """
    Ensure that lectures of the same course are in the same slots across all groups.
    """
    course_slots = {}
    for var in variables:
        if var.session_type == "lecture":
            if var.course in course_slots:  
                if var.slot != course_slots[var.course]:
                    return False
            else:
                course_slots[var.course] = var.slot
    return True