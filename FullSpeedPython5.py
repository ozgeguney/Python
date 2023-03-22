import DictionariesExamples

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

#nested dictionary
students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
      "Gibrael": {"age": 10, "address": "Sesimbra"},
      "Susan": {"age": 11, "address": "Lisbon"},
      "Charles": {"age": 9, "address": "Sesimbra"},
  }

print(DictionariesExamples.lengthDictionary(students))

print(DictionariesExamples.calculateAvg(ages))

print(DictionariesExamples.oldestStudent(ages))

print(DictionariesExamples.updateAges(ages, 10))

print(DictionariesExamples.totalStudents(students))

print(DictionariesExamples.calculateAverageAge(students))

print(DictionariesExamples.findStudents(students, 'Lisbon'))