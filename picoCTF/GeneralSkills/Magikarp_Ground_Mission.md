## Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`

Additional details will be available after launching your challenge instance.

```console

ssh ctf-player@venus.picoctf.net -p 59235

```

There is a 3 part flag on this machine.

first is on: 

/home/ctf-player/drop-in

1of3.flag.txt

second is one directory above:

/home/ctf-player

2of3.flag.txt

last is on the the root direcotry 

/~

3of3.flag.txt

Combine them and get the flag
