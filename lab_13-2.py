# Liam O'Hara

# Create a dictionary named grades
grades = {
   "assignment1": 100,
   "assignment2": 100,
   "assignment3": 100,
   "assignment4": 100,
   "assignment5": 100
}

# Print a list of just all the grades you received
print("All grades:", list(grades.values()))

# Print the name of each assignment in the dictionary on a separate line
print("Assignment names:")
for assignment in grades.keys():
   print(assignment)

# Print the name and grade you received on each assignment that you scored 70 or above on
print("Grades 70 and above:")
for assignment, grade in grades.items():
   if grade >= 70:
       print(assignment, "-", grade)

# Print the name and grade you received on each assignment that you scored 50 or below on
print("Grades 50 and below:")
for assignment, grade in grades.items():
   if grade <= 50:
       print(assignment, "-", grade)