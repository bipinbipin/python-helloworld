import json

students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(student):
    # student = {"name": name, "student_id": student_id, "title": "student"}
    students.append(student)


def save_file(student):
    # try:
        f = open("students.txt", "a")
        f.write(str(student) + "\n")
        f.close()

    # except Exception:
    #     print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            json_data = dict(student)
            add_student(json_data)
        f.close()
    except Exception:
        print("Could not read file")


# yield (not commonly used)
def read_students(f):
    for line in f:
        yield line

#the * implies a variable number of arguments
def var_args(name, *args):
    print(name)
    print(args)
# var_args("bipin", "loves python", None, "hello", True)


# the ** implies key value pair
def var_args_with_keys(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])
# var_args_with_keys("bipin", description="loves python", feedback=None, saying="hello", subscriber=True)


# student_list = get_students_titlecase()

# add_student("bipin", 11)
# add_student(name="dave", student_id=34)     #you can explicitly name the arguments
# add_student("mike")
# add_student("eric")

read_file()
print_students_titlecase()

enter_data = True
while(enter_data):
    enter_new = input("Enter new student (Y/N)")
    if str(enter_new).upper() == "Y":
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        student = {"name": student_name, "student_id": student_id, "title": "student"}
        add_student(student)
    else:
        enter_data = False

for student in students:
    save_file(student)


