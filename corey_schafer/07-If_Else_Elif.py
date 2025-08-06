print("-----------------------------------------------------")
print("IF ELSE ELIF")
print("-----------------------------------------------------")
print("SCENARIO 1: Standard IF ELIF ELSE")
language='Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'Javascript':
    print('Language is Javascript')
else:
    print('No match')

print("-----------------------------------------------------")
print("SCENARIO 2: Standard IF ELIF ELSE -> AND")
user='Admin'
print(" --- AND Scenario -> TRUE --- ")
logged_in=True
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
print("------------------")
logged_in=False
print(" --- AND Scenario -> FALSE --- ")
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
print("-----------------------------------------------------")
print("SCENARIO 3: Standard IF ELIF ELSE -> OR")
print(" --- OR Scenario -> TRUE  --- ")
logged_in=True
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
print(" --- OR Scenario -> FALSE  --- ")
logged_in=False
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
print("------------------")
print("-----------------------------------------------------")
print("SCENARIO 4: Standard IF ELIF ELSE -> NOT")
print(" --- NOT Scenario -> TRUE  --- ")
logged_in=True

if not logged_in:
    print("Please log in")
else:
    print("Welcome")
print("------------------")
print(" --- NOT Scenario -> FALSE  --- ")
logged_in=False
if not logged_in:
    print("Please log in")
else:
    print("Welcome")

print("-----------------------------------------------------")
print("SCENARIO 5: Object Identity")
print("Test if 2 objects have the same identity basically means if they are the same object in memory.")
print("What it means is that -> 2 object can be equal and not be the same object in memory.")
print("To determine the identity we use the `is` keyword.")
a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))
print(a is b)
print("-----------------------------------------------------")
print("SCENARIO 6: True/False -> Working with number that is 0")
condition=0
if condition:
    print("True")
else:
    print("False")
print("-----------------------------------------------------")
print("SCENARIO 7: True/False -> Working with number that is non zero")
condition=10
if condition:
    print("True")
else:
    print("False")
print("-----------------------------------------------------")











