


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
    
    "output": "Negatives Not Allowed:[-1]"
}
t8 = {
    "input": {
       "string" : '-1,-2'
    },
    
    "output": "Negatives Not Allowed:[-1, -2]"
}
t9 = {
    "input": {
       "string" : "//&\n1&2&3&\n5"
    },
    
    "output": 11
}
t10 = {
    "input": {
       "string" : "\n1,2,3\n5,6,8"
    },
    
    "output": 25
}
tests = []

tests.extend([t1,t2,t3,t4,t5,t6,t7,t8,t9,t10])

# Function

def Add(string_numbers):
    
    strip_string = string_numbers.strip()
    # Check for empty string
    
    if strip_string:
        if strip_string.startswith("//"):
            # Finding delimiter
            delimiter = strip_string[2]
            number_list = strip_string.split(delimiter)
            number_list.pop(0)
        else:
            # Replace "\n" with ","
            new_stripped = strip_string.replace("\n",",")
            # with default ',' delimiter
            number_list = new_stripped.split(',')
        
        # Filtering if in case ther is '' element
        number_list = list(filter(lambda x: bool(x), number_list))
        
        number_list = list(map(lambda x:int(x), number_list))
        
        # Getting list of negative numbers if there any
        negative_nums = list(filter(lambda x: x<0, number_list))
        
        if negative_nums:
            return (f"Negatives Not Allowed:{negative_nums}")
        else:
            addition = sum(number_list)
            return addition
                
        
            
    else:
        return 0



def Test_Function():
    count=0
    for test in tests:
        count+=1
        if Add(test["input"]["string"]) == test["output"]:
            
            print(f"Test{count} is passed")
        else:
            print(f"Test{count} is failed")

Test_Function()