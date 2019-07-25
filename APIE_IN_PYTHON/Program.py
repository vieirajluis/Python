# Step 1 - Create abstract base class
class employee():
     def determine_weekly_salary(self, weeklyHours, wage):
        raise NotImplementedError("This abstract method must be implemented by a subclass")

# Step 2 - Inherit from base & define calculation for permanent employee
class permanent (employee): # Inheritance
    def determine_weekly_salary(self, weeklyhours, wage): # Polymorphism
        salary = 40 * wage
        print("\nThis ANGRY EMPLOYEE worked " + str(weeklyhours) +
                " hrs. Paid for 40 hrs (no overtime) at $ " + str(wage) +
                            "/hr = $" + str(salary) + "\n")
        print("---------------------------------------------\n")

# Step 3 - Inherit from base & define calculation for contractor 
class contractor (employee): # Inheritance
    def determine_weekly_salary(self, weeklyhours, wage): # Polymorphism
        salary = weeklyhours * wage
        print("\nThis CONTRACTOR worked " + str(weeklyhours) +
            " hrs. Paid for " + str(weeklyhours) + " hrs (w/ overtime) at $ " + str(wage)
            + "/hr = $ " + str(salary) + "\n")


# Step 4 - Create permanent / contractor objects & list 
def get_employees(): # Encapsulation
    some_permanent_employee = permanent
    some_contractor = contractor
    everyone = [some_permanent_employee, some_contractor]
    return everyone


def main():
   # Step 5 - Polymorphically calculate salaries
    hours = 50;  wage = 70
    employees = get_employees() # Abstraction

    for  e in employees:
         e.determine_weekly_salary('self',hours, wage)
    

if __name__ == "__main__":
    main()