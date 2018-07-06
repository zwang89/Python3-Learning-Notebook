## 7. Common functions
### 1) **+=** function
*  **+=** is for current_line = current_line + 1
```Python
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
```

### 2) How to change a matrix in to a list?
* sometimes, we need to change a matrix to a flat, one row list. Here is the code and how.
```Python
myMatrix = [[1, 2, 3, 4],
            [5, 6, 7],
            [8, 9, 10]]
mylist_3 = []
# change the matrix to a list
#list comprehension, first read each subrow in myMatrix, then read each element in subrow.
flat_list = [i for sub in myMatrix for i in sub]
```

### 3) How to find all numbers in a **mixed** list?
* Situation: given a list that contains numbers and strings, how can we generate a list that only contains the numbers/list/other data type?

  In this situation, we need to use **isinstance(var, type)** function.
```Python
# for list comprehension, if there are multiple conditions, just add another if in the function.
is_num = [i for i in flat_list_2 if isinstance(i, int) if i % 2 == 0]
```

### 4) Import another .py file and use its function.
* In some cases, users want to first define all functions in one file and use it latter. Here is how: (see details in ex25.py file)

```Python
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the tifrst and last words of the sentece."""
    words= break_words(sentece)
    print_first_word(words)
    print_last_word(words)
```

In case you want to use the pre-defined function latter in another file:

```Python
sorted_mysentence = ex25.sort_sentence(mysentence)
print(sorted_mysentence)
```
### 5) What if multiple elif blocks are true?
* Python starts at the top and runs the first block that is true, so it will run only the first one.

### 6) What does **while loop** do?
* This makes an infinite loop. So, ... be careful!

### 7) Read a txt file into pandas, separate, and add headers

```pyython
# filepath is the location of files, the delimiter is the separater, names are the header names
df = pd.read_csv(filepath3, delimiter=':',
                 names=['ID', 'lag'])
```
