class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}"


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def get_details(self):
        return (
            f"{super().get_details()}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Salary: ${self.salary:.1f}"
        )


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def get_details(self):
        return f"{super().get_details()}\nDepartment: {self.department}"


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    people = []
    employees = []
    managers = []

    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter Name: ").strip()
            age = read_int("Enter Age: ")

            person = Person(name, age)
            people.append(person)

            print(f"Person created with name: {person.name} and age: {person.age}.")

        elif choice == "2":
            name = input("Enter Name: ").strip()
            age = read_int("Enter Age: ")
            employee_id = input("Enter Employee ID: ").strip()
            salary = read_float("Enter Salary: ")

            employee = Employee(name, age, employee_id, salary)
            employees.append(employee)

            print(
                f"Employee created with name: {employee.name}, age: {employee.age}, "
                f"ID: {employee.employee_id}, and salary: ${employee.salary:.1f}."
            )

        elif choice == "3":
            name = input("Enter Name: ").strip()
            age = read_int("Enter Age: ")
            employee_id = input("Enter Employee ID: ").strip()
            salary = read_float("Enter Salary: ")
            department = input("Enter Department: ").strip()

            manager = Manager(name, age, employee_id, salary, department)
            managers.append(manager)

            print(
                f"Manager created with name: {manager.name}, age: {manager.age}, "
                f"ID: {manager.employee_id}, salary: ${manager.salary:.1f}, "
                f"and department: {manager.department}."
            )

        elif choice == "4":
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")

            details_choice = input("Enter your choice: ").strip()

            records = {
                "1": ("Person", people),
                "2": ("Employee", employees),
                "3": ("Manager", managers),
            }.get(details_choice)

            if records is None:
                print("Invalid choice.")
                continue

            kind, objects = records

            if not objects:
                print(f"No {kind.lower()} records have been created yet.")
            else:
                for index, obj in enumerate(objects, start=1):
                    print(f"\n{kind} Details ({index}):")
                    print(obj.get_details())

        elif choice == "5":
            print("Exiting the system. All resources have been freed.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose an option from 1 to 5.")

        print("\n--- Choose another operation ---")


if __name__ == "__main__":
    main()