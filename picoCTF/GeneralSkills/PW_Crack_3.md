## Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

In the script we can see that there are 7 possible passwords:

```console

pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]

```
Because its a small number we can brute force it. Password is pos_pw_list[2].

