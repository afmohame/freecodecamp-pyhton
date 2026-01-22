def number_pattern(n):
    list_num = [n]
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n <= 0:
        return "Argument must be an integer greater than 0."
    
    else:
        for i in list_num:
            n -= 1
            list_num.append(n)
            if n == 1:
                list_num.reverse()
                break
        return " ".join(map(str, list_num))
    #join will take STRINGS and glue them together so if there was no " " it will glue 
    #them together like this 
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