students = []


class Student:                                      # parent class

    school_name = "Springfield Elementary"          # class variable / attribute

    def __init__(self, name, student_id=332):       # constructor
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):                              # to string method
        return "Student " + self.name

    def get_name_capitalize(self):                  # custom method
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

# mark = Student("Mark")
# print(mark)
# print(Student.school_name)


class HighSchoolStudent(Student):                   # child class (inherits 'Student')

    school_name = "Springfield High School"         # overridden attribute

    def get_name_capitalize(self):                  # overridden method
        orginial_value = super().get_name_capitalize()
        return orginial_value + " - HS"


james = HighSchoolStudent("james")
print(james.get_name_capitalize())

# NOTES

# python does not have access modifiers
#    some developers use underscore ('_some_method') to denote that a method should not be used or overridden
# python does not have interfaces
