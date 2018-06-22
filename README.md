# Python3 Learning Notebook
# Python Summary and Notes
### 1. print function
```python
print ("Print function sucks")
```
* purpose: this function is to print out the content included in the ( );
* **print** function can return calculation
```python
print ("do the math", 20 + 494 / 20)
```
* **format print** function print out and replace the varaible value the users give to the computer;
```python
print(f"what is {varaible}")
```
* **print** can also print out varaibles directly
```python
x = "give the value of x"
print (x)
```
* **print** can also feed values to value containers { };
```python
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
```
* If you want to print out multiple lines, just use
```python
print ("""
this is how we
print
out
\t multiple
lines
""")
```
Also, use \t to have a "tab" in the

  print (end = ' ' means print to the same line instead of a new line)

### 2. Add Notes and Read Codes
* Add any notes that is necessary for you to understand your code in latter time.
* **READ** your code backward from bottom to up will help you understand what the code is doing.

### 3. Ask users for data: **_input_** and **_argv_**
* **input** function is ask users for data
```Python
# the results will print ou as one line since we have the end option
print ("How olde are you?", end=' ')
age = input()
```
* **argv** is a function from sys package.
```Python
# import function to load library
from sys import argv
# read the wyss section for how to run this
script, first, second, third = argv
#
print ("the first script is called", script)
print ("the second script is called", first)
print ("the third script is called", second)
print ("the third script is called", third)
```

### 4. Open, and load, write and close your data
* sometimes, users are need to import (open a file) and read their data files. In python, two steps to complete this task:
   1. open the file by using **open** function;
   2. read the file by using **read** function;

 ```python
txt = open (filename, 'w') #write mode to open a file
txt.read()
#not necessary since open with 'write mode' will overwrite the file
target.truncate()
txt.close()
```
* One option of **.open** function is 'w', which means that open the file with write mode (overwrite).
* **.write** function is to write files directly to specific files
```python
# open to_file and create out_file
# write indate to out_file
out_file = open(to_file, 'w')
out_file.write(indata)
```

### 5. **_exists_** function from **os.path** package
* The **exists** function is to detect if specific files exisits. If does, 'TruGrammarGrammare' will return

### 6. Define a function
* In Python programming, you sometimes needs to define your own fuction to finish a task. The following check list is a wonderful summary from "Learn Python 3 the Hard Way";

> 1. Did you start your function definition with def?
> 2. Does our function name have only characters?
> 3. Did you put an open parenthesis right after a function name?
> 4. Did you put your arguments after the parenthesis separated by commas?
> 5. Did you make each argument unique (meaning no duplicated names)?
> 6. Did you put a close parenthesis and a colon after the arguments?
> 7. Did you indent all lines of code you want in the function four spaces? **no more, no less!**
> 8. Did you "end" your function by goinbg back to write with no ident?

* The author also provides reader with recall check list:

> 1. did you call/use/run this function by typing its name?
> 2. Did you put the ( character after the name to run it?
> 3. Did you put the values you want into the parentheses separated by commas?
> 4. Did you end the function call with a ) character?

* **return** in a function to print out/return the value that you want to print out
```Python
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b
```



### 7. Common functions
#### 1) **+=** function
*  **+=** is for current_line = current_line + 1
```Python
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
```
