# Subject names
subjects = ['Bangla', 'English', 'Math', 'Science']

# Taking input for each subject's marks
marks = []
for subject in subjects:
    marks.append(int(input("Enter marks for {}: ".format(subject))))

# Calculating average marks
average_marks = sum(marks) / len(marks)

if average_marks >= 91:
    grade = 'A+'
elif average_marks >= 81:
    grade = 'A'
elif average_marks >= 71:
    grade = 'B'
elif average_marks >= 61:
    grade = 'C'
elif average_marks >= 41:
    grade = 'D'
else:
    grade = 'F'


print("\nGrade Report:\nAverage Marks: {} \nYour Grade is: {}".format(average_marks, grade))
