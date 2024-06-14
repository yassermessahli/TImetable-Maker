class CSP:
    """The implementation of csp problem and its solution"""
    
    def __init__(self, variables: list, domains, constraints: list) -> None:
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        
    def __str__(self) -> str:
        return self.variables
    
    def is_complete(self) -> bool:
        for var in self.variables:
            if var.slot is None:
                return False
        return True
    
    def select_unassigned_variable(self):
        for var in self.variables:
            if var.slot is None:
                return var
    
    def is_consistent(self) -> bool:
        for constraint in self.constraints:
            if not constraint(self.variables):
                return False
        return True
    
    
    def domain_values(self, var) -> list:
        if isinstance(self.domains, dict):
            return self.domains[var]
        else:
            return self.domains
    
    
    def backtrack(self):
        if self.is_complete():
            return True
        variable = self.select_unassigned_variable()
        domain = self.domain_values(variable)
        for value in domain:
            variable.slot = value
            if self.is_consistent():
                result = self.backtrack()
                if result:
                    return result
        variable.slot = None
        return False
    
    def solve(self):
        result = self.backtrack()
        print(f"Solution Found: {result}")
        if result:
            for var in self.variables:
                print(var)
        
