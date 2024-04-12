

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for index in range(len(students)):
    print(students[index], 'has a grade of', grades[index], 'and their activity is', activities[index])

pass_fail = ['pass' if grade >= 80 else 'fail' for grade in grades]

print(pass_fail)

students.remove('Jane')
print (students)
print ('congrats you passed')