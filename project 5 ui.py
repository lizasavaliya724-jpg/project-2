import tkinter as tk
from tkinter import ttk, messagebox


class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}"


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id, self.salary = employee_id, salary

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


class PeopleApp:
    BG = "#eaf3ff"
    BLUE = "#2563eb"
    DARK = "#1e3a5f"

    def __init__(self, root):
        self.root = root
        self.root.title("People Management System")
        self.root.geometry("540x600")
        self.root.configure(bg=self.BG)
        self.root.resizable(False, False)

        self.records = {"Person": [], "Employee": [], "Manager": []}
        self.kind = tk.StringVar(value="Person")
        self.details_kind = tk.StringVar(value="Person")
        self.fields = {}

        self.setup_styles()
        self.build_ui()
        self.update_fields()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox", padding=6, fieldbackground="white")
        style.configure(
            "Blue.TButton",
            background=self.BLUE,
            foreground="white",
            padding=9,
            font=("Arial", 10, "bold"),
        )
        style.map("Blue.TButton", background=[("active", "#1d4ed8")])

    def build_ui(self):
        main = tk.Frame(self.root, bg=self.BG, padx=22, pady=18)
        main.pack(fill="both", expand=True)

        tk.Label(
            main,
            text="People Management System",
            bg=self.BG,
            fg=self.DARK,
            font=("Arial", 20, "bold"),
        ).pack(pady=(0, 16))

        form = tk.LabelFrame(
            main,
            text=" Create a record ",
            bg="white",
            fg=self.DARK,
            font=("Arial", 11, "bold"),
            padx=16,
            pady=12,
            bd=0,
            highlightthickness=1,
            highlightbackground="#d4e2f3",
        )
        form.pack(fill="x")

        self.add_row(form, "Record type", 0)
        type_box = ttk.Combobox(
            form,
            textvariable=self.kind,
            values=["Person", "Employee", "Manager"],
            state="readonly",
        )
        type_box.grid(row=0, column=1, sticky="ew", pady=5)
        type_box.bind("<<ComboboxSelected>>", self.update_fields)

        for row, field in enumerate(
            ["Name", "Age", "Employee ID", "Salary", "Department"], start=1
        ):
            label = tk.Label(form, text=field, bg="white", fg=self.DARK)
            entry = ttk.Entry(form)
            label.grid(row=row, column=0, sticky="w", pady=5, padx=(0, 12))
            entry.grid(row=row, column=1, sticky="ew", pady=5)
            self.fields[field] = (label, entry)

        form.columnconfigure(1, weight=1)

        ttk.Button(
            form, text="Create Record", style="Blue.TButton", command=self.create_record
        ).grid(row=6, column=0, columnspan=2, sticky="ew", pady=(12, 2))

        details = tk.LabelFrame(
            main,
            text=" Show details ",
            bg="white",
            fg=self.DARK,
            font=("Arial", 11, "bold"),
            padx=16,
            pady=12,
            bd=0,
            highlightthickness=1,
            highlightbackground="#d4e2f3",
        )
        details.pack(fill="both", expand=True, pady=(16, 0))

        ttk.Combobox(
            details,
            textvariable=self.details_kind,
            values=["Person", "Employee", "Manager"],
            state="readonly",
        ).pack(fill="x", pady=(0, 9))

        ttk.Button(
            details,
            text="Show Details",
            style="Blue.TButton",
            command=self.show_details,
        ).pack(fill="x")

        self.output = tk.Text(
            details,
            height=8,
            wrap="word",
            bg="#f8fbff",
            fg="#24364b",
            relief="flat",
            padx=10,
            pady=10,
            font=("Arial", 10),
            state="disabled",
        )
        self.output.pack(fill="both", expand=True, pady=(10, 0))

    def add_row(self, parent, text, row):
        tk.Label(parent, text=text, bg="white", fg=self.DARK).grid(
            row=row, column=0, sticky="w", pady=5, padx=(0, 12)
        )

    def update_fields(self, _event=None):
        visible = {
            "Person": {"Name", "Age"},
            "Employee": {"Name", "Age", "Employee ID", "Salary"},
            "Manager": {"Name", "Age", "Employee ID", "Salary", "Department"},
        }[self.kind.get()]

        for field, (label, entry) in self.fields.items():
            if field in visible:
                label.grid()
                entry.grid()
            else:
                label.grid_remove()
                entry.grid_remove()
                entry.delete(0, tk.END)

    def create_record(self):
        kind = self.kind.get()
        try:
            name = self.fields["Name"][1].get().strip()
            if not name:
                raise ValueError("Please enter a name.")

            age = int(self.fields["Age"][1].get().strip())

            if kind == "Person":
                obj = Person(name, age)
            else:
                employee_id = self.fields["Employee ID"][1].get().strip()
                salary = float(self.fields["Salary"][1].get().strip())
                if not employee_id:
                    raise ValueError("Please enter an employee ID.")

                if kind == "Employee":
                    obj = Employee(name, age, employee_id, salary)
                else:
                    department = self.fields["Department"][1].get().strip()
                    if not department:
                        raise ValueError("Please enter a department.")
                    obj = Manager(name, age, employee_id, salary, department)

            self.records[kind].append(obj)
            messagebox.showinfo("Created", f"{kind} record created for {name}.")
            for _, entry in self.fields.values():
                entry.delete(0, tk.END)

        except ValueError as error:
            messagebox.showerror(
                "Invalid input", str(error) or "Please check the entered values."
            )

    def show_details(self):
        kind = self.details_kind.get()
        objects = self.records[kind]

        if objects:
            result = "\n\n".join(
                f"{kind} Details ({i}):\n{obj.get_details()}"
                for i, obj in enumerate(objects, start=1)
            )
        else:
            result = f"No {kind.lower()} records have been created yet."

        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, result)
        self.output.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = PeopleApp(root)
    root.mainloop()