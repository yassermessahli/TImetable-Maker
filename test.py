from csp import CSP


def constraint1(assignment, var, value):
    return (var == "A" and value != assignment.get("B", None)) or (var == "B" and value != assignment.get("A", None)) or var in ["C", "D"]


def constraint2(assignment, var, value):
    return (var == "A" and value == assignment.get("D", value)) or (var == "D" and value == assignment.get("A", value)) or var in ["B", "C"]

def constraint3(assignment, var, value):
    return (var == "C" and value < assignment.get("D", value+1)) or (var == "D" and value > assignment.get("C", value-1)) or var in ["A", "B"]

def constraint4(assignment, var, value):
    return (var == "C" and value < assignment.get("B", value+1)) or (var == "B" and value > assignment.get("C", value-1)) or var in ["A", "D"]



variables = ['A', 'B', 'C', 'D']
domains = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3],
    'D': [1, 2, 3],
}
constraints = [constraint1, constraint2, constraint3, constraint4]


csp = CSP(variables, domains, constraints)
solution = csp.backtrack()
print(solution)
