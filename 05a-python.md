# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> A tuple can be defined by a values separated with commas while a list is a set of numbers or strings separated by commas within `[]`. Lists are defined with square brackets `[]`, whereas tuples are represented with parentheses `()`. While both data types can be indexed and nested, tuples are immutable (individual assignment is not possible). However, tuples can contain lists that are mutable. Tuples are better suited as keys in dictionaries as they immutable, and are unlikely to disrupt key:value pairs in a dictionary.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are an unordered data type within curly brackets whereas lists are an ordered data type within square brackets. Duplicates are removed in sets whereas duplicates are maintained in lists. As lists are ordered (every value is associated with a position) and contain duplicates, sets enable faster membership testing over lists. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is a small anonymous 'single expression' function. See example below:
```
nested_list = [(5, 6, 7, 8), (1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6), (4, 5, 6, 7)]
nested_list.sort(key=lambda tuple: tuple[0])
print(nested_list)
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is the ability to create a list by including an expression followed by a `for` clause, followed by any number of `for` or `if` clauses. 
```
# Here is a list of numbers for pH range
def x_v(p):
    return p
# Using list comprehension
print([x_v(x) for x in range(1,15)])
# Using filter and map functions
print(list(filter(x_v, range(1, 15))))
print(list(map(x_v, range(1, 15))))
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> **Answer:** 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> **Answer:** 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> **Answer:** 7850 days  

For answer, please see code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
For answer, please see the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
For answer, please see the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





