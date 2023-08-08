import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

def main():
    # Read employee data from the JSON file
    with open('employee.json', 'r') as file:
        employee_data = json.load(file)

    employee_objects = []
    for emp_info in employee_data:
        emp = Employee(emp_info["Name"], emp_info["DOB"], emp_info["Height"], emp_info["City"], emp_info["State"])
        employee_objects.append(emp)

    # Print the list of Employee objects
    for emp in employee_objects:
        print(f"Name: {emp.name}, DOB: {emp.dob}, Height: {emp.height}, City: {emp.city}, State: {emp.state}")

if __name__ == "__main__":
    main()
