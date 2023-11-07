## Figure out how they moved the flag.

Open it with wireshark.

Go to File-Export Object-TFTP.

Select 'Save All'

The files are:
 instructions.txt  picture1.bmp  picture2.bmp  picture3.bmp  plan  program.deb

Use rot13 to decode 'instruction' and 'plan'.

instructions:
 TFTP DOESN T ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

plan:
 I USED THE PROGRAM AND HIDIT WITH -DUEDILIGENCE. CHECK OUT THE PHOTOS

The 'program.deb' is seghide. You can install it from here or from your own package manager.

```console

steghide extract -sf picture3.bmp

```
It will spit out flag.txt.

