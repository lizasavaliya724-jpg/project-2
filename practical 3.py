class Student:
    def __init__(self, student_id, name, age, grade, dob, subjects):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.dob = dob
        self.subjects = subjects

    def __str__(self):
        return f"Student ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Grade: {self.grade} | Subjects: {', '.join(self.subjects)}"


class StudentDataOrganizer:
    def __init__(self):
        self.students = {}

    def add_student(self):
        print("\nEnter student details:")
        student_id = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")
        subjects = [s.strip() for s in subjects]

        self.students[student_id] = Student(student_id, name, age, grade, dob, subjects)
        print("\n Student added successfully!\n")

    def display_students(self):
        print("\n--- Display All Students ---")
        if not self.students:
            print("No students available.\n")
        else:
            for student in self.students.values():
                print(student)
        print()

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        if student_id in self.students:
            student = self.students[student_id]
            print("Enter new details (leave blank to keep old value):")

            name = input(f"Name ({student.name}): ") or student.name
            age = input(f"Age ({student.age}): ") or student.age
            grade = input(f"Grade ({student.grade}): ") or student.grade
            dob = input(f"Date of Birth ({student.dob}): ") or student.dob
            subjects = input(f"Subjects ({', '.join(student.subjects)}): ")
            subjects = [s.strip() for s in subjects.split(",")] if subjects else student.subjects

            self.students[student_id] = Student(student_id, name, age, grade, dob, subjects)
            print("\n Student updated successfully!\n")
        else:
            print(" Student not found.\n")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print("\n Student deleted successfully!\n")
        else:
            print(" Student not found.\n")

    def display_subjects(self):
        print("\n--- Subjects Offered ---")
        subjects = set()
        for student in self.students.values():
            subjects.update(student.subjects)
        if subjects:
            print(", ".join(subjects))
        else:
            print("No subjects available.")
        print()


def main():
    organizer = StudentDataOrganizer()
    print(" Welcome to the Student Data Organizer!\n")

    while True:
        print("Select an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            organizer.add_student()
        elif choice == "2":
            organizer.display_students()
        elif choice == "3":
            organizer.update_student()
        elif choice == "4":
            organizer.delete_student()
        elif choice == "5":
            organizer.display_subjects()
        elif choice == "6":
            print("\n Thank you for using the Student Data Organizer. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()