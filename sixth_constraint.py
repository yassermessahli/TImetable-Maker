from variables_domains import Slot, days, slots_per_day, CourseSession , all_slots , groups , courses , variables

def max_two_days_per_teacher(variables: list):
    # Create a dictionary to track the days each teacher is assigned
    teacher_days = {}

    for var in variables:
        # Get the teacher of the current CourseSession
        teacher = var.teacher
        
        # Check if the teacher already has days assigned
        if teacher in teacher_days:
            teacher_days[teacher].append(var.slot.day)
            # If the teacher already has two days assigned, return False
            if len(set(teacher_days[teacher])) > 2:
                return False
            # Otherwise, add the current day to the list of assigned days for the teacher
            
            

        else:
            # If the teacher has no assigned days, initialize the list with the current day
            teacher_days[teacher] = [var.slot.day]

        print(teacher_days[teacher])

    return True


#test the function

print(variables[1].teacher)
print(variables[22].teacher)
print(variables[43].teacher)

variables[1].slot = Slot(day='Sunday', time=1)
variables[22].slot = Slot(day='Monday', time=2)
variables[43].slot = Slot(day='Monday', time=3)

print(max_two_days_per_teacher([variables[1],variables[22],variables[43]]))