```python
for i in s:
    statements
```
The variable **$\color{green}{i}$** is known as the **$\color{green}{iteration\ variable}$**. On each iteration of the loop, it receives a new value from s. The scope of the iteration variable is not private to the for statement. If a previously defined variable has the same name, that value will be overwritten. Moreover, the iteration variable retains the last value after the loop has completed.
If the elements produced by iteration are iterables of identical size, you can unpack their values into seperate iteration variables using a statement such as this:
```python
for i in s:
    statements
```


> __Note__ 
> test    
> 
> __Warning__


