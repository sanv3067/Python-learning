projects = {
    "Project A": ["Ganapathi", "Bala", "Ibu"],
    "Project B": ["Ganapathi", "Kishor"],
    "Project C": ["Ibu","Ganapathi"]
}

count = {}

for employees in projects.values():
    for employee in employees:
        count[employee] = count.get(employee, 0) + 1

for employee, n in count.items():
    if n >= 1:
        print(employee, "works in", n, "projects")