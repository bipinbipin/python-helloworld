student_names = "James,Katarina,Bort,Frank,Dave,Bob,Max,Ed".split(',')

for name in student_names:
    if name == "Bort":
        print("Found him! " + name)
        break
    print("currently testing " + name)

