student_id = (101,102,103,104,105,106,107,108,108,109,110)
duplicate_list = []
for student in student_id:
    if student_id.count(student) > 1 and student not in duplicate_list:
        duplicate_list.append(student)
        print("duplicate ID :",student)
