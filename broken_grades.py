'''
    Name: Shafaq Mandha 
    MISIS: M00914211
    Module: PDE1130
    SOB no. 31
'''
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing. 

exam_one = int(input("Input exam grade one: "))


exam_two = int(input("Input exam grade two: "))
'''
    -	The error in the above code was that an additional parenthesis was added in the end.
    -	Since the input taken by the user is supposed to be an integer value I set the string value as int(input(" ")).

'''

exam_three = int(input("Input exam grade three: "))
'''
    -	Changed the "str" to "int". Since the input taken by the user is supposed to be an integer value I set the string value as int(input(" ")).
    -	Changed the variable name "exam_3" to "exam_three" to match the variable name of that mentioned in the array.

'''

grades = [exam_one, exam_two, exam_three]
# Added a comma between the variable names in the array.

total_grade = 0 # "sum is already a predefined functon in python so there I changed the variable name to total_grade
for grade in grades: # Changed "grade" to "grades" as the correct variable name is set as "grades" and "grade" undefined.
    total_grade = total_grade + grade
avg = total_grade / len(grades) # Changed "grdes" to "grades" since we need to take the length of the array grades and the array grdes does not exist

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
    '''
        Corrections made in above two lines:
            - Added a colon as it was missing causing a syntax error.
    '''
elif avg >= 70 and avg < 80:
    letter_grade = "C"
    '''
        Corrections made:
            - Changed single quotation at the end of C to double quotations.
            - Changed the range from "avg > 69 and avg < 80" to "avg >= 70 and avg < 80"
    '''

elif avg >= 60 and avg < 70:
    letter_grade = "D"
    '''
        Corrections made:
            - Changed the range from "avg <= 69 and avg >= 65" to "avg >= 60 and avg < 70"
    '''
else: # Changed "elif" to "else".
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
