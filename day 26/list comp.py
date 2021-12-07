import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student_names:random.randint(1, 100) for student_names in
                  names}
print(student_scores)
passed_students = {pstudent_names:student_scores[pstudent_names] for
                   pstudent_names in student_scores if student_scores[
                       pstudent_names] >= 60 }
print(passed_students)