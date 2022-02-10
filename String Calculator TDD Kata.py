


# Test Cases

from audioop import add


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

tests = []

tests.extend([t1,t2,t3,t4,t5,t6,t7])

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
            number_list = strip_string.split(',')
        
        number_list = list(map(lambda x:int(x), number_list))
        
        # Getting list of negative numbers if there any
        negative_nums = list(filter(lambda x: x<0, number_list))
        
        if negative_nums:
            return f"Negatives not allowed"
        else:
            addition = sum(number_list)
            return addition
                
        
            
    else:
        return 0



def Test_Function():
    count=0
    for test in tests:
        count+=1
        if Add(test["input"]["string"])== test["output"]:
            
            print(f"Test{count} is passed")
        else:
            print(f"Test{count} is failed")

Test_Function()