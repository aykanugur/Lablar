import random
import string
mydict = {}
passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

    
while True: 
    for i in range(5):
        x = input("Enter a lowercase character: ").lower()
        
        if (x in string.punctuation):
            print("'{}' is not suitable for key Choose another letter.".format(x))
            continue

        if x in mydict:
            print("'{}' is already in the dictionary. Choose another letter.".format(x))
            continue
    

        mydict[x] = [] 

        for j in range(3):
            while True:
                y = input("Enter a replacement for '{}': ".format(x))
                if((x in string.punctuation) == False):
                    print("'{}' is not suitable for replacement. Choose another letter.".format(y))
                    continue
                    
                if any(y in replacements for replacements in mydict.values()): #bunu ögrenmedik önceden biliyorum.
                    print("'{}' is already used as a replacement for another letter. Enter a different character.".format(y))
                else:
                    mydict[x].append(y) 
                    break 
        
    break
strong = list()
weak = list()
for x in passwords:
    changes = 0
    for y in x:
        if(mydict.__contains__(y)):
         changes += 1
         newList = mydict[y]
         key = random.choice(newList)
         x = x.replace(y, key)
         print("CHANGED")
    if(changes >4):
        strong.append(x)
    else:
        weak.append(x)
print("strong passwords:")
for x in strong:
    print(x)
print("weak passwords:")
for x in weak:
    print(x)
    
        

