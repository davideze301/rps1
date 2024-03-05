name="Dave"
count=1
def greetings(firstname):
    color="blue"
   
    print(color)
    print(firstname)
greetings("Victoria ")

def another():
    color="blue"
    global count
    count +=1
    print(count) 
    
    
    
    
    def greetings(name):
        nonlocal color
        color="red"
        print(color)
        print(name)
    greetings("Dave")
another()
        
