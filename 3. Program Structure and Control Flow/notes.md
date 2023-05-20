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
Eventhough it is most common to see this used when s is a sequence of tuples, unpacking works when the items in s are any kind of iterable, including lists, generators, and strings.

If the items produced by an iterable have varying sizes, you can use wildcard unpacking to place multiple values into a variable. For example:
```python
s = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
for x, y, *extra in s:
    statements
# x = 1, y = 2, extra = []
```

```python
for i, x in enumerate(s):
    statements
```
enumerate(s) creates an iterator that produces tuples (0, s[0]), (1, s[1]) and so on    
A different starting value for the count can be provided  with the start keyword argument
```python
for i, x in enumerate(s, start=100):
    statements
```
In this case, tuples of the form (100, s[0]), (101, s[1]) will be produced

iterating in parallel
```python
for x, y in zip(s, t):
    statements
```
zip combines iterables s and t into an iterable of tuples (s[0], t[0]), (s[1], t[1]) 
If you want the result converted to a list, use list(zip(s, t))
```python
a = [1,2,3]
b = [1,2,3,4,5,6]
print(list(zip(a, b)))
>>> [(1, 1), (2, 2), (3, 3)]
```

looplardaki continue ile ilgili:

```python
for (...)
{
   if (!cond1)
   {
      if (!cond2)
      {
          ... highly indented lines ...
      }
   }
}
```
yerine 
```python
for (...)
{
   if (cond1 || cond2)
   {
      continue;
   }

   ...
}
```

bir de 

```python
if some condition:
    pass
else:
    statement
```
yerine
```python
if some condition:
    coninue
statement
```
hatta
```python
if not some condition:
    statement
```

**$\color{red}{Python\ does\ not\ provide\ a\ "goto"\ statement}$**.









> __Note__ 
> test  
> 
> __Warning__


