## There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc jupiter.challenges.picoctf.org 44566.

For this we will use an interger overflow. THe max value for an int in C is 2147483647

When we connect with nc and try to buy a cheep flag out account ballance is changing. We can use that in order to overflow first bite. For that we have to find the magic number witch is max int value / price of the flag:

2147483647 / 900 = 2386092.94111 

In order to overflow we need to make this number a bit larger, something like 2387092

If we buy that many flags, the account ballance would overflow and give us a large number from witch we can buy the real flag.



