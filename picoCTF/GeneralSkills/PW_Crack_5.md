## Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. Here's a dictionary with all possible passwords based on the password conventions we've seen so far.

It's the same as Crack4 but with an external list. If we change the code we can get:

```python

import hashlib

correct_pw_hash = open('level5.hash.bin', 'rb').read()


                                                                                    
def hash_pw(pw_str):                                                               
    pw_bytes = bytearray()                                                         
    pw_bytes.extend(pw_str.encode())                                               
    m = hashlib.md5()                                                              
    m.update(pw_bytes)                                                             
    return m.digest()



dictionary = open("dictionary.txt", "r").readlines()

for i in dictionary:
	if hash_pw(i.strip()) == correct_pw_hash:
		print(i.strip())

```
This will give us the password.
