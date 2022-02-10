


# Test Cases

t1 = {
    "input":{
        "string":""
    },
    
    "output":0
}

t2 = {
    "input": {
        "string":'1'
    },
    
    "output":1
}
t3 = {
    "input": {
        "string":'1\n2'
    },
    
    "output":3
}
t4 = {
    "input": {
        "string":'1\n2,3'
    },
    
    "output":6
}
t5 = {
    "input": {
        "string":'1\n2,\n3'
    },
    
    "output":6
}
t6 = {
    "input": {
        "string":'//;1;2'
    },
    
    "output":3
}
t7 = {
    "input": {
        "string":'//;-1;'
    },
    
    "output": "Negative not allowed"
}



# Function

def Add(string_numbers):
    
    strip_string = string_numbers.strip()
    # Check for empty string
    
    if strip_string:
        if strip_string.startswith("/"):
            # Finding delimiter
            delimiter = strip_string[2]
            number_list = strip_string.split(delimiter)
            
        else:
            # with default ',' delimiter
            number_list = strip_string.aplit(',')
            
    else:
        return 0



