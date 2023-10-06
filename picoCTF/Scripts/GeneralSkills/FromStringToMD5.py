import hashlib                                                                      
import sys                                                                          
                                                                                     
def generate_md5_hash(string):                                                      
    md5_hash = hashlib.md5(string.encode()).hexdigest()                             
    return md5_hash                                                                 
                                                                                     
# Check if an argument is provided                                                  
if len(sys.argv) > 1:                                                               
    argument = sys.argv[1]                                                          
    md5_hash = generate_md5_hash(argument)                                          
    print(md5_hash)                                                                 
else:                                                                               
    print("Please provide an argument.")
