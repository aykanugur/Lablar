
print("What is your name")
name = input()
print("Hello {0}".format(name))
print("What is your Student ID? ")
student_id = input()
print("Your ID is {0}".format(student_id))

print("enter val1")
val1 = float(input())
print("enter val2")
val2 = float(input())
sum = val1 + val2
diff = val1 - val2
prod = val1 * val2
print("sum : {0}".format(sum))
print("diff : {0}".format(diff))
print("prod : {0}".format(prod))

total = 0
print("Enter your name : ")
name = input()
print("Enter your lab score")
labgrade  = input()
total = total + float(labgrade) * 0.25
print("Enter your midterm grade : ")
midterm = input()
total = total + float(midterm) * 0.35
print("Enter your final grade : ")
finalgrade = input()
total = total + float(finalgrade) * 0.40

print("Name: {0}".format(name))
print("Lab score: {0}".format(labgrade))
print("Midterm: {0}".format(midterm))
print("Final grade: {0}".format(finalgrade))
print("Total: {0}".format(total))

print("*\n**\n***\n**\n*")
