## Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag in the same directory too.

When you open the script, I notice the condition for the password:

```console

if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):

```

If we put that in a python shell we get:

```console

de76

```

Use that as password and we get out flag.
