import math_utils as mu

input1= int(input())
input2 = int(input())

print("enter operator")
print('operator list : + = add , - subtract , * multiply , / divide , ** power , % mod ')
operator = input()

selectedOperator = {
    '+' : mu.add,
    '-' : mu.subtract,
    '*' : mu.multiply,
    '**' : mu.power,
    '%' : mu.mod,
    '/' : mu.divide
}

selected2=selectedOperator.get(operator)
print(selected2(input1,input2))

if __name__ == "__main__":
    print('work in main')
    
