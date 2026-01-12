num = int(input("Number of test cases? "))
for i in range(num):
    school = input("School? ")
    N = int(input("Students: "))
    student_gpa = {}
    for i in range(N):
        student = input()
        start = False
        course = []
        total_hours = 0
        grade_points = 0
        name = ""
        for k in student:
            if start:
                course.append(k)
            if k == ":":
                start = True
            if start == False:
                name += k
        value = course[0::3]
        hours = course[1::3]
        for k in hours:
            total_hours += int(k)
        for k in range(len(value)):
            if value[k] == "A":
                grade_points += 4 * int(hours[k])
            elif value[k] == "B":
                grade_points += 3 * int(hours[k])
            elif value[k] == "C":
                grade_points += 2 * int(hours[k])
            else:
                grade_points += 1 * int(hours[k])
            
        gpa = grade_points / total_hours
        student_gpa[name] = gpa
        

    vali = max(student_gpa, key=student_gpa.get)
    print(school, "=", vali)

        
