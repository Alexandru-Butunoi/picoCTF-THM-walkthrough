## Fix the syntax error in this Python script to print the flag. Download Python script

If we run it we get:

```
  File "/home/alex/Downloads/PICO/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent

```

If we delete the space in last line we get:

```

flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)

```

Now, if we run it we get the flag.


