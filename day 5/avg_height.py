# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆
sum_of_students = 0
for height in student_heights:
    sum_of_students = sum_of_students + int(height)
no_of_students = 0
for height in student_heights:
    no_of_students = int(no_of_students) + 1
avg_height = sum_of_students / no_of_students
print(f"the average height is {round(avg_height)}")
#Write your code below this row 👇
