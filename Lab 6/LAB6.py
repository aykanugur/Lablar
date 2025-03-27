import math



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
func = lambda x,y: x**(2*y+1)/factorial(2*y+1) if y % 2 ==0 else x**(2*y+1)/factorial(2*y+1) * -1
def sine_x(x,n):
    result = 0
    x = x*math.pi/180
    for i in range(n):
        result += func(x,i)
    print(result)
    
    
globalVal = 0
def question3(n):
    global globalVal
    if n > 0:
        globalVal += 1/n 
        question3(n-1)
    else:
        print(globalVal)
    
        
        
    

    
print("ENTER VAL 1: ", end="")
Input1 = int(input());
print("ENTER VAL 2: ", end="")
Input2 = int(input());
sine_x(Input1,Input2)

    
    
    
    
    
    
    