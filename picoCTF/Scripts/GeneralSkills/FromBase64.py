import sys                                                                                     
import base64                                                                                  
                                                                                               
# Check if the script receives a string as an argument                                         
if len(sys.argv) > 1:                                                                          
    input_string = sys.argv[1]                                                                 
    encoded_bytes = input_string.encode('utf-8')                                               
    base64_text = base64.b64decode(encoded_bytes).decode('utf-8')                              
    print("Base64 to Text:", base64_text)                                                      
else:                                                                                          
    print("Please provide a string as an argument.") 
