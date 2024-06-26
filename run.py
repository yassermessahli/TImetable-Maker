from csp import CSP
from constraints import *
from variables_domains import variables, all_slots
from random import shuffle
import time
from output.visualise import visualise_timetable



if __name__ == "__main__":
   
   # Setup
   variables = variables
   domains = all_slots
   constraints = [no_more_than_three_successive, 
                  no_same_slot_different_courses, 
                  no_same_slot_lectures,
                  same_slot_for_lectures_of_same_course,
                  no_same_slot_different_groups_same_td,
                  ]

   start_time = time.time()

   print("shuffling...")
   # shuffle(variables)
   shuffle(domains)
   shuffle(constraints)

   print("solving...\n")
   csp = CSP(variables, domains, constraints)
   csp.solve()
   visualise_timetable(variables)


   end_time = time.time()
   execution_time = end_time - start_time
   print(f"code run with execution time: {round(execution_time, 4)} seconds")