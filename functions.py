def hello_world():
    print("hello world !")
    
    
    
hello_world()

def sum(num1=0,num2=0):
    if(type(num1)is not int or type(num2)is not int):
        return 0
    return num1+num2
    
    
    
total=sum(9,9)
print(total)




def multiple_items(*args):
    print(args)
    print(type(args))
multiple_items("david","ugonna","eze ")
    
    
def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
multi_named_items(first="david" ,last="ugonna")
    
    
    

    