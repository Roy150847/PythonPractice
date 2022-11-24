total = int(input(" Enter the total number of days: "))
present = int(input(" Enter the number of days present: "))
per = present * 100 / total
if per >= 75 :
    print(" The candidate is eligible to take the exams ")
else :
    print(" The candidate is not eligible to take the exams ")
    