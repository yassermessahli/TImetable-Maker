from variables_domains import Slot, days, slots_per_day, CourseSession , all_slots , groups , courses , variables


def max_three_groups_same_tp_session(*args):
    """
    we are going to check if the same slot is not allocated to more than 3 groups for the same tp course with different teachers
    cuz there is a 3 available teachers for each tp course
    """ 

    # Create a dictionary to track tp sessions for each course at each slot
    tp_sessions = {}

    for arg in args:
        # Check if the session type is "tp"
        if arg.session_type == "tp":
            # Check if the course already has tp sessions at the slot
            if arg.slot in tp_sessions:
                # If the course already has tp sessions, check if there are already 3 groups assigned
                if len(tp_sessions[arg.slot][arg.course]) >= 3:
                    return False
                # Check if the teacher for the current session is the same as the ones already assigned
                elif arg.teacher in tp_sessions[arg.slot][arg.course]:
                    return False
                else:
                    # Otherwise, record the teacher for the session
                    tp_sessions[arg.slot][arg.course].append(arg.teacher)
            else:
                # If there are no tp sessions at the slot, initialize the course and teacher list
                tp_sessions[arg.slot] = {arg.course: [arg.teacher]}

    return True




#test the function

print(variables[-1].teacher)
print(variables[-23].teacher)

variables[-1].slot = Slot(day='Sunday', time=1)
variables[-23].slot = Slot(day='Sunday', time=1)

print(max_three_groups_same_tp_session(variables[-1],variables[-23])) # True

variables[-1].slot = Slot(day='Sunday', time=1)
variables[-23].slot = Slot(day='Sunday', time=1)
variables[-23].teacher = "Teacher 14"

print(max_three_groups_same_tp_session(variables[-1],variables[-23])) # False


