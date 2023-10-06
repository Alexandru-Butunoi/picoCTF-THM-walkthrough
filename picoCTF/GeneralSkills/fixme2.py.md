## Fix the syntax error in the Python script to print the flag. Download Python script

If we run it we get:

```

  File "/home/alex/Downloads/PICO/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?


```

So all we have to do is to replace '=' with '=='

```

# Check that flag is not empty
if flag == "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)

```

Now if we run it we get the flag
