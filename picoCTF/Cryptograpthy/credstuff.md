## We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it? Download the leak here. The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

So we got a list of usernames and passwords that are in order. 

If first user has the first password then to find cultiris's password we just have to find the list number.

A simple search shows that his place is 378 with password cvpbPGS{P7e1S_54I35_71Z3}

This looks like a rotation cipher so let's try (cyberchef.org)[https://cyberchef.org/] for it.

With ROT13 we get : 

picoCTF{C7r1F_54V35_****}
