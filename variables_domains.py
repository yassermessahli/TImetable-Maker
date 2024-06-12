
from collections import namedtuple

# Define a namedtuple for slots
Slot = namedtuple('Slot', ['day', 'time'])

# Define the days and the time slots for each day
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
slots_per_day = {
    "Sunday": [1, 2, 3, 4, 5],
    "Monday": [1, 2, 3, 4, 5],
    "Tuesday": [1, 2, 3],
    "Wednesday": [1, 2, 3, 4, 5],
    "Thursday": [1, 2, 3, 4, 5]
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

# Define the groups and their courses
groups = range(1, 7)
courses = [
    ("Sécurité", "lecture", "Teacher 1"),
    ("Sécurité", "td", "Teacher 1"),
    ("Méthodes formelles", "lecture", "Teacher 2"),
    ("Méthodes formelles", "td", "Teacher 2"),
    ("Analyse numérique", "lecture", "Teacher 3"),
    ("Analyse numérique", "td", "Teacher 3"),
    ("Entrepreneuriat", "lecture", "Teacher 4"),
    ("Recherche opérationnelle 2", "lecture", "Teacher 5"),
    ("Recherche opérationnelle 2", "td", "Teacher 5"),
    ("Distributed Architecture & Intensive Computing", "lecture", "Teacher 6"),
    ("Distributed Architecture & Intensive Computing", "td", "Teacher 6"),
    ("Réseaux 2", "lecture", "Teacher 7"),
    ("Réseaux 2", "td", "Teacher 7"),
    ("Réseaux 2", "tp", ["Teacher 8", "Teacher 9", "Teacher 10"]),
    ("Artificial Intelligence", "lecture", "Teacher 11"),
    ("Artificial Intelligence", "td", "Teacher 11"),
    ("Artificial Intelligence", "tp", ["Teacher 12", "Teacher 13", "Teacher 14"])
]

# Create variables for the problem
variables = []
for group in groups:
    for course, session_type, teacher in courses:
        if isinstance(teacher, list):  # Handle multiple teachers for TP sessions
            for tp_teacher in teacher:
                variables.append(CourseSession(group, course, session_type, tp_teacher))
        else:
            variables.append(CourseSession(group, course, session_type, teacher))


print(variables)