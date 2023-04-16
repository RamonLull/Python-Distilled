```python
for i in s:
    statements
```
The variable **$\color{green}{i}$** is known as the **$\color{green}{iteration\ variable}$**. On each iteration of the loop, it receives a new value from s. The scope of the iteration variable is not private to the for statement. If a previously defined variable has the same name, that value will be overwritten. Moreover, the iteration variable retains the last value after the loop has completed.
````python
i = "this won't stay"
for i in range(5):
    pass
print(i)
>>> 4
````
If the elements produced by iteration are iterables of identical size, you can unpack their values into seperate iteration variables using a statement such as this:
```python
s = [(1, 2, 3), (4, 5, 6)]
for x, y, z in s:
    statements
```

> __Note__ 
> test  
> 
> __Warning__


