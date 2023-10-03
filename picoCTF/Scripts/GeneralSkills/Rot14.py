import sys                                                                                     
                                                                                                
def rot14(text):                                                                               
    result = ""                                                                                
    for char in text:                                                                          
        if char.isalpha():                                                                     
            ascii_offset = ord('a') if char.islower() else ord('A')                            
            shifted_ascii = (ord(char) - ascii_offset + 14) % 26 + ascii_offset                
            result += chr(shifted_ascii)                                                       
        else:                                                                                  
            result += char                                                                     
    return result                                                                              
                                                                                                
 # Check if the script receives a string as an argument                                         
if len(sys.argv) > 1:                                                                          
    input_string = sys.argv[1]                                                                 
    encrypted_string = rot14(input_string)                                                     
    print("Encrypted string:", encrypted_string)                                               
else:                                                                                          
    print("Please provide a string as an argument.") 
