## Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam. Can you help us identify whose mail server the email actually originated from? Download the email file here. Flag: picoCTF{FirstnameLastname}


Open the email in text editor and find permitted sender at line 34:

 173.249.33.206 as permitted sender) client-ip=173.249.33.206;

Use whois to find the name:

```

whois 173.249.33.206

```

