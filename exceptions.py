student = {
    "name": "Bipin",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Butala"  #adds a new key and value

try:
    last_name = student["last_name"]    #this line throws a "KeyError" exception (without line 7)
    numbered_last_name = 3 + last_name  #this throws a "TypeError" exception
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I cannot add these two types together")
    print(error)
except Exception:
    print("Unknown Error")

print("code continues to execute")
