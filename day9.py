student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
grades = {
    range(91, 100): "Outstanding",
    range(81, 90): "Exceeds Expectations",
    range(71, 80): "Acceptable",
    range(0, 70): "Fail"
}

student_grades = {}

for key in student_scores:
    student_grades = student_scores[key] + grades[student_scores]
    print(student_grades)