a = "hello world"
print(repr(a))

with open('data.txt') as file:
  for line in file:
    print(line, end='')