def how_much_teacher_assigned(teacher: str, variables: list) -> int:
    return len([var for var in variables if var.teacher == teacher and var.slot])


def time_number_to_name(time_number: int) -> str:
    return f"Slot {time_number}"


def group_number_to_name(group_number: int) -> str:
    return f"G{group_number}"


def rename_day(day: str) -> str:
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    return f"{days.index(day)+1}) {day}"
