ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
     "Thomas": 10,
     "Bob": 10,
     "Joseph": 11,
     "Maria": 12,
     "Gabriel": 10,
  }
print(ages["Peter"])
print(ages)

#to get both keys and values using "items()"
for key, value in ages.items():
    print(key, value)

#only key
for x in ages:
    print(x)
#only values
for x in ages:
    print(ages[x])
#another method to get only values
for x in ages.values():
    print(x)


new_dict = dict()
new_dict2 = {}
ages2 = dict()
ages2["Peter"] = 9
ages2["Susan"] = 10
for key, value in ages2.items():
    print(key, value)

from collections import OrderedDict
ages3 = OrderedDict()
ages3["Peter"] = 0
ages3["Susan"] = 1
ages3["Maris"] = 2

for key, value in ages3.items():
    print(key, value)

d = {
    0: [1,2,3],
    1: [2,3,4],
    2: [3,4,5]
}
print(d[1])

#nested dictionary
students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
      "Gibrael": {"age": 10, "address": "Sesimbra"},
      "Susan": {"age": 11, "address": "Lisbon"},
      "Charles": {"age": 9, "address": "Sesimbra"},
  }

print(students)
print(students["Anna"])
print(students["Anna"]["age"])
print(students["Anna"]["address"])

print(list(students.values())[0]["age"])

for student_name, value in students.items():
    print("\nStudent Name:", student_name)
    for key in value:
        print(key, ":", value[key])

def lengthDictionary(Students):
  return len(Students)

def calculateAvg(ages):
  return sum(ages.values()) / len(ages)

def oldestStudent(ages):
  values = list(ages.values())
  keys = list(ages.keys())
  max_value = max(values)
  index = values.index(max_value)
  key = keys[index]
  return key

def updateAges(ages, n):
  new_ages = {}
  for index, values in ages.items():
    values = values +n
    new_ages[index] = values
  return new_ages

def totalStudents(students):
  return(len(students.keys()))

def calculateAverageAge(students):
    sum = 0
    for thing in students.values():
        age = thing['age']
        sum = sum + age
    return (sum / len(students.keys()))

def findStudents(students, address):
    result = []
    for key, value in students.items():
        if value["address"] == address:
            result.append(key)
    return sorted(result)

