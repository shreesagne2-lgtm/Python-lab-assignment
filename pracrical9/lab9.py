class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    def __init__(self, name, age, salary, address):
        super().__init__(name, age, salary, address)


managers = []

for i in range(2):  # change to 10 if required
    print("\nEnter details of Manager", i+1)

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))
    address = input("Enter Address: ")

    m = Manager(name, age, salary, address)
    managers.append(m)

print("\nManager Details")
for m in managers:
    m.display()
    print("----------------")