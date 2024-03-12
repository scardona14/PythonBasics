import time
print("This program will generate a grade according to the percentage you get on a exam.")
time.sleep(1)

print("")
name_of_exam=input("Please, type the anme of exam subject: ")
time.sleep(1)

print("")
max_score=int(input("Please, type the maximum score of the exam: "))
time.sleep(1)

print("")
your_score=int(input("Please, type the score you got: "))
time.sleep(1)

print("")
grade_in_percentage = round((your_score * 100)/max_score, 1)

print("Exam Grade Generator")
time.sleep(1)
print("Name of the exam subject: " + name_of_exam)
time.sleep(1)
print("Max. Possible Score: " + str(max_score))
time.sleep(1)
print("Your score: " + str(your_score))
time.sleep(1)
print("You got " + str(grade_in_percentage) + "% which is a grade of ")

if grade_in_percentage >= 90:
  print("A+")
  elif_grade_in_percentage >= 80 and grade_in_percentage <= 89:
  print("A")
elif grade_in_percentage >= 70 and grade_in_percentage <= 79:
  print("B")
elif grade_in_percentage >= 60 and grade_in_percentage <= 69:
  print("C")
elif grade_in_percentage >= 50 and grade_in_percentage <= 59:
  print("D")
else:
  print("U")