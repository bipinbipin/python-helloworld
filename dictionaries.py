import json

student = {
    "name": "Bipin",
    "student_id": 15163,
    "feedback": None
}
print(student)

#List of Dictionaries
all_students = [
    {"name": "Bipin", "student_id": 15163, "feedback": None},
    {"name": "Eric", "student_id": 15164, "feedback": None},
    {"name": "Tony", "student_id": 15165, "feedback": None},
    {"name": "Josh", "student_id": 15166, "feedback": None}
]
print(all_students)

#Dictionary Data
print(student["name"])
print(student.keys())
print(student.values())

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

pp_json(all_students)
