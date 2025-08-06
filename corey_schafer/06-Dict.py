print("-----------------------------------------------------")
print("Dictionary")
print("In Python, a dictionary is a built-in data type that allows you to store key-value pairs.")
print("KEY CHARACTERSTICS:")
print("1. Each item in a dictionary has a key and a value.")
print("2. Keys must be unique and immutable (e.g., strings, numbers, tuples).")
print("3. Values can be any data type and can repeat.")
print("4. Dictionaries are unordered before Python 3.7, but maintain insertion order from Python 3.7+.")
print("-----------------------------------------------------")
print("SCENARIO 1: To access the entire dictionary or a specific value inside the dictionary")
student= {'name':'John','age':25, 'courses':['Math','CompSci']}
print("To access the entire dictionary:")
print(student)
print("To access a specific value inside the dictionary:")
print(student['name'])
print(student['courses'])
print("If you specify the name of the key directly in the dictionary -> This will return error")
print("-----------------------------------------------------")
print("SCENARIO 2: Using get()")
print("One benefit of using get() instead of specifying the name of the dictionary is that")
print("If the name of the key doesnt exist in dictionary -> If you pass name of the key in the dictionary -> we will get error. This is where we use get()")
print("If the name of the key doesnt exist in dictionary -> If we call the get() -> This will return `None` by default.")
student= {'name':'John','age':25, 'courses':['Math','CompSci']}
print("You can customize it by passing a default message as shown below:")
print(student.get('phone','Not Found'))
print("-----------------------------------------------------")
print("SCENARIO 3: Assigning value by specifying key -> If the key exist + Reassigning a different value for a key")
student= {'name':'John','age':25, 'courses':['Math','CompSci']}
student['phone']='555-5555'
student['name']='Jane'
print(student)
print("-----------------------------------------------------")
print("SCENARIO 4: Using update() method -> this is to ADD/ UPDATE values in the dictionary.")
print("This is much more efficient to do rather than manually placing the values in SCENARIO 3")
student= {'name':'John','age':25, 'courses':['Math','CompSci']}
student.update({'name':'Jakarta','age':34,'courses':['History','Geography']})
print(student)
print("-----------------------------------------------------")
print("SCENARIO 5: Using `del` keyword -> This is used to delete a specific key in the dictionary.")
student= {'name':'John','age':25, 'courses':['Math','CompSci']}
del student['age']
print(student)
print("-----------------------------------------------------")
print("SCENARIO 6: Using pop() method.")
student= {'name':'John','age':25, 'courses':['Math','CompSci']}
age=student.pop('age')
print(student)
print(age)
print("-----------------------------------------------------")
print("SCENARIO 7: keys() method -> To display only keys inside the dictionary")
student= {'name':'John','age':25, 'courses':['Math','CompSci']}
print(student.keys())
print("-----------------------------------------------------")
print("SCENARIO 8: values() method -> To display only values inside the dictionary")
student= {'name':'John','age':25, 'courses':['Math','CompSci']}
print(student.values())
print("-----------------------------------------------------")
print("SCENARIO 9: items() method -> To display key and value pairs inside the dictionary")
student= {'name':'John','age':25, 'courses':['Math','CompSci']}
print(student.items())
print("-----------------------------------------------------")
print("SCENARIO 10: Using for loop to loop through items() method")
student= {'name':'John','age':25, 'courses':['Math','CompSci']}
for key, value in student.items():
    print(key, " - > ", value)
print("-----------------------------------------------------")
























