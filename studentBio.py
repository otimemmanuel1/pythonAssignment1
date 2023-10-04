'''
Use an account with your full names
'''



#python program to display student biodata after being entered into this program
print('Enter your biodata please')
students = []
print('\n')
for i in range(0,9):
      name = str(input('Enter you name: '))
      students.append(name)
      regNo = str(input('Enter your registration number: '))
      students.append(regNo)
      age = int(input('Enter your age: '))
      students.append(age)
      course = str(input('Enter your course: '))
      students.append(course)
      yearOfStudy = int(input('Enter your Year of study: '))
      students.append(yearOfStudy)
      graduationYear = int(input('Enter your expected year of graduation: '))
print(students)
