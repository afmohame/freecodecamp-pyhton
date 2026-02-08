def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n <= 0:
        return "Argument must be an integer greater than 0."
    else:
        list_num = range(1, n+1, 1)
        return " ".join(map(str, list_num))
    #join will take STRINGS and glue them together so if there was no " " it will glue 
    #them together like this:
    #12345
    #map will turn each variable into the desired func or data type 
    
try1 = number_pattern(4)
try2 = number_pattern(12)
try3 = number_pattern(-34)
try4 = number_pattern("12")
try5 = number_pattern("hello")

print(try1)
print(try2)
print(try3)
print(try4)
print(try5)