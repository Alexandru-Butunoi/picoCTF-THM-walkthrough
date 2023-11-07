## I've hidden a flag in this file. Can you find it? Forensics is fun.pptm

Unzip the file:

```console

unzip Forensics\ is\ fun.pptm


```

Go to ppt/slideMasters
 
 there is a file called 'hidden'

```console

cat hidden

>>> Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q

```

Trim it and decode it with base64:

```console

cat hidden | sed 's/ //g' | base64 -d 

```
