### First push of large files
```
git init
git lfs install
git lfs track "*.mp4"
git add .gitattributes
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/LUK34/ASK-DATAENG-PYTHON.git
git push -u origin main
```

### Successive update
```
git lfs track
git add .
git commit -m " "
git push origin main
```

# corey_schafer python basics
- **Method - It is a function that is only available to a specific data type**
- E.g: the below example is a **Multi-line strings**. This enhances readability
```
"""Mr. and Mrs. Dursley,
of number four Private Drive,
were proud to say that they were perfectly normal
"""
````

### 01-textData.py
- The programme will explore the following:
- how to display a specific character from the string/ range of characters from the string 
- lower() - To print lower case letters
- upper() - To print upper case letters
- count() - Takes the entire string passed as an argument
- find() -> To find the starting position of the string that is passed as an argument
- replace() -> To replace the given string with the another string

- Placeholder
```
message2= '{}, {}. Welcome!'.format(greeting, name)
print(message2)
```

- f string for python version > 3.6
```
print("f string for python version > 3.6: ")
message3 = f'{greeting}, {name.upper()}. Welcome!'
print(message3)
```

- help() function -> you need to run the help function on a string class then only it will work.
```
print("help() function -> you need to run the help function on a string class then only it will work.")
print(help(str))
print(help(str.lower))
```

### 02-NumericData.py
- The programme will explore the following:
- how to idenify the numeric data is `int` or `float`
- Arthimetic Operations

- abs() -> It is a built-in function that returns the absolute value of a number.
- It means the distance from zero, regardless of the sign (positive or negative).

- round() -> It is used to round a number to the nearest integer or to a specified number of decimal places.

- Comparison operator
- Type Conversion / Type Casting

### 03-List.py

- **split()**
```string.split(separator, maxsplit)```
```
info = "name-age-location"
result = info.split("-", 1)
print(result)
```
- Output
```
['name', 'age-location']
```


### Difference between list and tuple
- **1. Mutability**
- List: Mutable (can be changed after creation)
```
my_list = [1, 2, 3]
my_list[0] = 10  # ✅ Allowed
```
- Tuple: Immutable (cannot be changed after creation)
```
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # ❌ Error: 'tuple' object does not support item assignment
```
- **2. Syntax**
- List: Uses square brackets []
```
[1, 2, 3]
```
- Tuple: Uses parentheses ()
```
(1, 2, 3)
```
- **3. Performance**
- Tuple is faster than list when iterating or accessing elements.
- Use tuples when data shouldn't change to gain performance benefits.

- **4. Use Cases**
- List: When you need a dynamic collection that can be modified.
- Tuple: When you need a fixed collection (e.g., coordinates, function returns).

- **5. Methods Available**
- List: Has more built-in methods (e.g., .append(), .remove(), .sort())
- Tuple: Only a few methods (e.g., .count(), .index())


### 04-Tuple.py


### 05-Set.py



### 06-Dict.py
- In Python, a dictionary is a built-in data type that allows you to store key-value pairs.
- **Key Characteristics:**
- Each item in a dictionary has a key and a value.
- Keys must be unique and immutable (e.g., strings, numbers, tuples).
- Values can be any data type and can repeat.
- Dictionaries are unordered before Python 3.7, but maintain insertion order from Python 3.7+.
- **SCENARIO 1:** To access the entire dictionary or a specific value inside the dictionary
- **SCENARIO 2:** Using get()
- **SCENARIO 3:** Assigning value by specifying key -> If the key exist + Reassigning a different value for a key
- **SCENARIO 4:** Using update() method -> this is to ADD/ UPDATE values in the dictionary.
- **SCENARIO 5:** Using `del` keyword -> This is used to delete a specific key in the dictionary.
- **SCENARIO 6:** Using pop() method.
- **SCENARIO 7:** keys() method -> To display only keys inside the dictionary
- **SCENARIO 8:** values() method -> To display only values inside the dictionary
- **SCENARIO 9:** items() method -> To display key and value pairs inside the dictionary
- **SCENARIO 10:** Using for loop to loop through items() method










