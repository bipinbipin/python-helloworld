# import classes    # here you have to refer to your methods with full syntax (i.e. classes.HighSchoolStudent)
# from classes import HighSchoolStudent  # here you are importing just one class from file

from classes import *

bipin = HighSchoolStudent("bipin")
print(bipin.get_name_capitalize())