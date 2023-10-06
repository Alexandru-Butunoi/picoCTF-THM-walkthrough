import sys                                                                          
                                                                                     
def decimal_to_binary(decimal_num):                                                 
    binary_num = bin(decimal_num).replace("0b", "")                                 
    return binary_num                                                               
                                                                                     
# Check if the argument is provided                                                 
if len(sys.argv) != 2:                                                              
    print("Please provide a decimal number as an argument.")                        
else:                                                                               
    try:                                                                            
        decimal_number = int(sys.argv[1])                                           
        binary_number = decimal_to_binary(decimal_number)                           
        print(binary_number)                                                        
    except ValueError:                                                              
        print("Invalid decimal number provided.") 
