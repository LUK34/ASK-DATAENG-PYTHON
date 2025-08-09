## Intermediate python

### os module
- To work with files and directories without manually opening File Explorer or Terminal.
- To read/write environment variables.
- To run system commands from Python.
- To detect OS type (Windows, Linux, macOS).

```
import os

print(os.getcwd())           # Get current working directory
os.mkdir("test_folder")      # Create new directory
os.chdir("test_folder")      # Change current directory
print(os.getcwd())           # Show new current directory
os.chdir("..")               # Go back to parent directory
os.rmdir("test_folder")      # Remove empty directory

files = os.listdir(".")      # List everything in current directory
print(files)

path = os.path.join("folder", "file.txt")  
print(path)                  # folder/file.txt (Windows: folder\file.txt)

print(os.path.exists("folder"))  # Check if path exists
print(os.path.isfile("file.txt")) # Check if it's a file
print(os.path.isdir("folder"))    # Check if it's a directory

print(os.environ.get("PATH"))        # Get PATH variable
os.environ["MY_VAR"] = "Hello World" # Set environment variable

os.system("echo Hello from Python")  # Run a terminal command

```

### Example of module
- Another useful module is datetime, which allows you to create and work with dates and times, as well as time zones and time periods!
- The datetime module has a function called date.
- In this exercise, you'll practice importing and using the date method from the datetime module and use it to create a variable.

```
# Import date from the datetime module
from datetime import date

# Create a variable called deadline
deadline = date(2024, 1, 19)

# Check the data type
print(type(deadline))  # <class 'datetime.date'>

# Print the deadline
print(deadline)        # 2024-01-19
```

### Packages
- creating collections of files. These collections are known as packages.
- We might also hear them referred to as libraries. Packages are publicly available, free of charge! 
- We can use packages in the same way as Python's built-in modules, with one extra step. 
- To access a package, we first need to download it from the Python Package Index, known as PyPI, which is essentially a directory of packages. 
- Afterwards, we can import the package, or parts of a package, using the same approach as we took when working with modules.


### Panda
- In Python, Pandas is a data analysis and manipulation library that makes it easy to work with structured data like tables (rows and columns), similar to Excel or SQL.
```
python3 -m pip install pandas
```
- **What it is**
- **Name:** pandas (stands for “Python Data Analysis”)
- **Type:** Open-source Python library
- **Purpose:** Handle, clean, analyze, and visualize data efficiently.


- **Key Features**
- **Data structures:**
- Series → 1-dimensional labeled data (like a column in Excel)
- DataFrame → 2-dimensional labeled data (like an Excel sheet or SQL table)
- **Data import/export:**
- Read/write CSV, Excel, JSON, SQL databases, etc.
- **Data cleaning:**
- Handle missing values, duplicates, incorrect data types
- **Data analysis:**
- Filtering, grouping, summarizing
- **Time series support:**
- Built-in functions for dates and time-based data.

```
# Import pandas using an alias
import pandas as pd

# Sales dictionary
sales = {"user_id": ["KM37", "PR19", "YU88"],
"order_value": [197.75, 208.21, 134.99]}

# Convert to a pandas DataFrame
sales_df = pd.DataFrame(sales)
sales_df

# Reading in a CSV file in our current directory
sales_df = pd.read_csv("sales.csv")
# Checking the data type
type(sales_df)

# DataFrame method to preview the first five rows
sales_df.head()

```

### Functions versus methods
- Function = code to perform a task
- Method = a function that is specific to a data type

```
import pandas as pd

# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first five rows
print(sales_df.head())
```

```
# Read in sales.csv
sales_df = pd.read_csv("sales.csv")

# Print the mean order_value
print(sales_df["order_value"].mean())

# Print the total value of sales
print(sales_df["order_value"].sum())
```

```
# Create the clean_string function
def clean_string(text):
  
  # Replace spaces with underscores
  no_spaces = text.replace(" ", "_")
  
  # Convert to lowercase
  clean_text = no_spaces.lower()
  
  # Return the final text as an output
  return clean_text

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)

```

### What is Docstrings in python
- In Python, docstrings (documentation strings) are string literals used to describe what a module, class, function, or method does.
- They’re meant for humans, not the Python interpreter — 
- so they help you (and others) understand the purpose and usage of the code without digging into the implementation.

```
def greet(name):
    """
    Greets the user by name.
    
    Parameters:
        name (str): The name of the person to greet.
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"
```

- ** Where Docstrings Can Be Used**
- Modules
```
"""This module handles user authentication and profile management."""
```
- Functions / Methods
```
def square(num):
    """Return the square of a number."""
    return num ** 2
```
- Classes
```
class Animal:
    """A simple class to represent an animal."""
```

- **Why Use Docstrings?**
- Improves code readability
- Generates documentation automatically (via tools like help(), Sphinx, or IDEs)
- Provides quick hints in interactive environments (e.g., Jupyter Notebook, Python REPL)

```
# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  
  	
  """
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data
```

- **What is arbitary arguments**
- In Python, arbitrary arguments let you pass a variable (unknown) number of arguments to a function.

- There are two main types:
- **Arbitrary Positional Arguments**
- Lets your function accept any number of positional arguments.
- Inside the function, args is a tuple.
```
def add_numbers(*args):
    """Add any number of numbers."""
    return sum(args)

print(add_numbers(2, 3))         # 5
print(add_numbers(2, 3, 4, 5))   # 14
```
- **Arbitrary Keyword Arguments**
- Lets your function accept any number of keyword arguments.
- Inside the function, kwargs is a dictionary.
```
def print_info(**kwargs):
    """Print key-value pairs passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, country="USA")

```
- **Mixing Arbitary Positional Arguments and Arbitary Keyword Arguments:**
- You can use both in the same function:
```
def demo_func(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

demo_func(1, 2, 3, name="Bob", age=30)
```

- example of arbitary positional argument
```
# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))
```

- example of arbitary keyword arguments
```
# Define a function called concat
def concat(**kwargs):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))

```

### Lambda function
- A lambda function in Python is a small, anonymous function — meaning it has no name (unless you assign it to a variable) and is typically used for short, throwaway operations.
- It’s defined using the keyword lambda instead of def.
```
lambda arguments: expression
```
- **Code example:**
```
# Normal function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

print(add_lambda(5, 3))  # 8
```
- **Example 1:**
```
sale_price = 29.99

# Define a lambda function called add_tax
add_tax = lambda x: x * 1.2

# Call the lambda function
print(add_tax(sale_price))
```
- **Key Features**
- Can take any number of arguments, but only one expression.
- Often used with functions like map(), filter(), and sorted().
- They’re inline and don’t require a formal def statement.
- **map()**
```
nums = [1, 2, 3, 4]
squares = list(map(lambda n: n**2, nums))
print(squares)  # [1, 4, 9, 16]
```
- **filter()**
```
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)  # [2, 4]
```
- **sorted()**
```
data = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # [(3, 'a'), (1, 'b'), (2, 'c')]

```

- **Example 2: Writing lambda function in a single line of code**
```
sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x: x * 1.2)(sale_price))
```

- **Example 3: Using map function**
```
sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = (map(lambda x: x*1.2, sales_prices))

# Create the updated list, sales_plus_tax
sales_plus_tax = list(add_taxes)

# Print the new list with updated values
print(sales_plus_tax)
```

### What is an error?
- An error occurs when we try to run code that violates a rule. Python has many different types of errors.
- We may also hear errors called exceptions—these terms have the same meaning.
- An error will cause our program to terminate, so our code should try to avoid its occurrence where possible!

- **TypeError**
- Let's look at a couple of common errors. 
- First is TypeError, which generally occurs when we try to use an incompatible data type when performing a task. 
- Here, we try to add a string and an integer and get an error message that this action is not supported on these two data types.

- **ValueError**
- There is ValueError, which occurs when a value provided is not within an acceptable range.
- For example, we get a ValueError if we try to convert the string "Hello" to a float. 
- This differs from a TypeError, because no error is produced if we call float and provide the number two as a string.

- **Tracebacks**
- Notice that the error outputs mentions the word "Traceback"? A traceback can be thought of as a report,
- providing information including what type of error occurred, in this case a ValueError,

### What are the different ways of handling error??

- **SCENARIO 1:**
- Using try / except / else / finally
- **else** runs if no exception occurs.
- **finally** always runs (good for cleanup).

```
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found!")
else:
    print("File opened successfully.")
finally:
    print("Done (cleanup).")
```

- **SCENARIO 2:Raising Exceptions (raise)**
- If you want to manually trigger an error:
```
def withdraw(amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    print(f"Withdrawing {amount}")

withdraw(-50)  # Raises ValueError
```

- **SCENARIO 3:Assertions (assert)**
- Quick way to enforce conditions during debugging.
```
x = 5
assert x > 0, "x must be positive"
```

- **SCENARIO 4: Context Managers for Safe Cleanup**
- Avoids errors when working with resources like files or network connections:
```
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File missing.")
```

- **SCENARIO 5: Logging Errors Instead of Printing**
```
import logging
logging.basicConfig(level=logging.ERROR)

try:
    10 / 0
except ZeroDivisionError as e:
    logging.error("Division error occurred", exc_info=True)
```


- **Example 1: **
```
def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.swap(" ", "_")
    clean_text = clean_text.lower()
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")
```

- **Example 2: **
```
def snake_case(text):
  # Check the data type
  if type(text) == str:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")
```