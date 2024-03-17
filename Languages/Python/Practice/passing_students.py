students = [("Alice", 75), 
            ("Bob", 55), 
            ("Charlie", 90), 
            ("David", 65), 
            ("Emma", 80)]


passed_students = [(name, grade) for name, grade in students if grade > 60]

for name, grade in passed_students:
    print(f"{name} passed with a grade of {grade}%")
