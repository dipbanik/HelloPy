students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student['name'].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {'name': name, 'student_id': student_id}
    students.append(student)


def save_file(student):
    try:
        f = open('students.txt', 'a')
        f.write(student + '\n')
        f.close()
    except Exception:
        print('Could not save file')


def read_file():
    try:
        f=open('students.txt', 'r')
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print('Could not read file')


'''
def var_args(name, *args):
    print(name)
    print(args)


var_args('Mark', 'Loves Python', None, "Hello")

'''
'''

def var_args(name, **kwargs):
    print(name)
    print(kwargs['description'], kwargs['feedback'])

var_args('Mark', description='Loves Python', feedback=None, subscription=True)

'''
read_file()
print_students_titlecase()

student_list = get_students_titlecase()

add_student(student_id=15, name='Mark')

while True:

    student_name = input('Enter student name:')
    student_id = int(input('Enter student id'))

    add_student(student_name, student_id)
    print_students_titlecase()

    cont = input("Continue? Y/N :")
    if cont == 'N':
        save_file(student_name)
        print('Bye Bye !!!')
        break
    elif cont == 'Y':
        save_file(student_name)
        continue
    else:
        save_file(student_name)
        print("Continuing as there was a wrong input")




