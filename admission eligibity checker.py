
#  take marks and percentage from user 
marks = float(input("Enter the marks obtained: "))
total_marks = float(input("Enter the total marks: "))
percentage = (marks / total_marks) * 100
print(f"Your percentage is: {percentage:.2f}%")
if percentage >= 60:
    print("Congratulations! You are eligible to apply for admission in the college.")
else:
     print("Sorry, you are not eligible to apply for the admission in the college.")
