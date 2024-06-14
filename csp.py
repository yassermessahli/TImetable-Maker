class CSP:
    """The implementation of csp problem and its solution"""
    
    def __init__(self, variables: list, domains: dict, constraints: list) -> None:
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}
        
    def __str__(self) -> str:
        return self.variables
    
    def is_complete(self) -> bool:
        return len(self.assignment) == len(self.variables)
    
    def select_unassigned_variable(self):
        for var in self.variables:
            if var not in self.assignment:
                return var
        return None
    
    def is_consistent(self, var, value) -> bool:
        for constraint in self.constraints:
            if not constraint(self.assignment, var, value):
                return False
        return True
    
    
    def domain_values(self, var) -> list:
        return self.domains[var]
    
    
    def backtrack(self):
        if self.is_complete():
            return self.assignment
        variable = self.select_unassigned_variable()
        domain = self.domain_values(variable)
        for value in domain:
            if self.is_consistent(variable, value):
                self.assignment[variable] = value
                result = self.backtrack()
                if result is not None:
                    return result
                del self.assignment[variable]
        return None
    
    