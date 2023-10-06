## Find the flag in the Python script! Download Python script

The function for the flag is in the script but it's never used:

```console

def print_flag():
  flag = str_xor(flag_enc, 'enkidu')
  print(flag)

```

We can call it after obtion b:

```console

 elif choice == 'b':
      print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
      print_flag()

```

Now, when we chouse b we call the flag as well.
