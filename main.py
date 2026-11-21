print("==================================")
print("    STUDENT MARK CALCULATOR    ")
print("==================================")
print("Welcome to the Student Mark Calculator!")
student_name=input("Enter student name: ")
print("Welcome,",student_name)
print("\nEnter your marks")
def get_mark(subject):
    while True:
        try:
            mark = int(input("Enter " + subject + " mark: "))

            if mark >= 0 and mark <= 100:
                return mark
            else:
                print("Invalid mark! Enter between 0 and 100.")

        except ValueError:
            print("Please enter numbers only!")


python_mark = get_mark("Python")
java_mark = get_mark("Java")
english_mark = get_mark("English")
maths_mark = get_mark("Maths")
physics_mark = get_mark("Physics")

total = python_mark+java_mark+english_mark+maths_mark+physics_mark
percentage = (total/500)*100

print("Total: ",total)
print("Percentage",percentage)
if python_mark>=35 and java_mark>=35 and english_mark>=35 and maths_mark>=35 and physics_mark>=35:
    result="PASS"
    if percentage>=90:
       grade="A+"
    elif percentage>=80:
        grade="A"
    elif percentage>=70:
        grade="B"
    elif percentage>=60:
        grade="C"
    elif percentage>=50:
        grade="D"
    else:
        grade="E"
else:
    result="FAIL"
    grade="F"
    
print("\n========================================")
print("           STUDENT REPORT")
print("========================================")
print("Student Name :", student_name)
print("----------------------------------------")
print("Python       :", python_mark)
print("Java         :", java_mark)
print("English      :", english_mark)
print("Maths        :", maths_mark)
print("Physics      :", physics_mark)
print("----------------------------------------")
print("Total Marks  :", total, "/ 500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("Result       :", result)
print("========================================")
print("               Thank you!               ")
print("========================================")
    
    
    
