## Static ain't always noise

# Can you look at the data in this binary: static? This BASH script might help!

 We get two files ltdis.sh and static

 The first is a bash script and if we run it with the second file, we get a file named static.ltdis.strings.txt

```console

bash ltds.sh static

```

 We search in on that file and we find the flag:

picoCTF{d15a5m_t34s3r_98d35***}

 Or we can just use 'strings' on static:

```console

strings static | grep pico 

```

 
