from collections import namedtuple
from pprint import pprint

# Define a namedtuple for slots
Slot = namedtuple("Slot", ["day", "time"])

# Define the days and the time slots for each day
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
slots_per_day = {
    "Sunday": [1, 2, 3, 4, 5],
    "Monday": [1, 2, 3, 4, 5],
    "Tuesday": [1, 2, 3],
    "Wednesday": [1, 2, 3, 4, 5],
    "Thursday": [1, 2, 3, 4, 5],
}

# Generate all possible slots
all_slots = [Slot(day, time) for day in days for time in slots_per_day[day]]


# Define the class for variables
class CourseSession:
    def __init__(self, group, course, session_type, teacher):
        self.group = group
        self.course = course
        self.session_type = session_type
        self.teacher = teacher
        self.slot = None

    def __repr__(self):
        return f"{self.group}_{self.course}_{self.session_type}_{self.teacher}"

    def __str__(self):
        return f"Group: {self.group}, Course: {self.course}, Type: {self.session_type}, Teacher: {self.teacher}, Slot: {self.slot}"

# Define the groups and their courses
groups = range(1, 7)
courses = [
    ("Sécurité", "lecture", "Teacher 1"),
    ("Méthodes formelles", "lecture", "Teacher 2"),
    ("Analyse numérique", "lecture", "Teacher 3"),
    ("Entrepreneuriat", "lecture", "Teacher 4"),
    ("Recherche opérationnelle 2", "lecture", "Teacher 5"),
    ("Distributed Architecture & Intensive Computing", "lecture", "Teacher 6"),
    ("Réseaux 2", "lecture", "Teacher 7"),
    ("Artificial Intelligence", "lecture", "Teacher 11"),
    ("Sécurité", "td", "Teacher 1"),
    ("Méthodes formelles", "td", "Teacher 2"),
    ("Analyse numérique", "td", "Teacher 3"),
    ("Recherche opérationnelle 2", "td", "Teacher 5"),
    ("Distributed Architecture & Intensive Computing", "td", "Teacher 6"),
    ("Réseaux 2", "td", "Teacher 7"),
    ("Artificial Intelligence", "td", "Teacher 11"),
    ("Réseaux 2", "tp", ["Teacher 8", "Teacher 9", "Teacher 10"]),
    ("Artificial Intelligence", "tp", ["Teacher 12", "Teacher 13", "Teacher 14"]),
]

# returns the number of sessions assigned to a teacher
def how_much_teacher_assigned(teacher: str, variables: list) -> int:
    return [v.teacher for v in variables].count(teacher)

# Create variables for the problem
variables = []
for group in groups:
    for course, session_type, teacher in courses:
        if isinstance(teacher, list):  # Handle multiple teachers for TP sessions
            # there are 3 tp teachers for each tp session, and 6 groups
            # so each teacher takes 2 groups
            for tp_teacher in teacher:
                # if the teacher is assigned to less than 2 sessions, assign him to the current session
                if how_much_teacher_assigned(tp_teacher, variables) < 2:
                    variables.append(CourseSession(group, course, session_type, tp_teacher))
                    break
        else:
            variables.append(CourseSession(group, course, session_type, teacher))


# print only tp sessions
# print("== TP Sessions: ==")
# for v in variables:
#     if v.session_type == "tp":
#         print(v)