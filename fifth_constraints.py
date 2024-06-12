def same_slot_for_lectures_of_same_course(args):
    """
    Ensure that lectures of the same course are in the same slots across all groups.
    """
    
    course_slots = {}

    for arg in args:
        
        if arg.session_type == "lecture":
            if arg.course in course_slots:
                
                if arg.slot != course_slots[arg.course]:
                    return False
            else:
                
                course_slots[arg.course] = arg.slot

    return True