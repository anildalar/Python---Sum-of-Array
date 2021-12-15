#1. Lets create the empty list

nums = [] # List

for x in range(100):
    numbers = input("Please Enter some numbers ")
    #print(numbers)
    if numbers == '':
        break
    nums.append(int(numbers))


print(nums)


'''
while True :
    numbers = input("Please Enter some numbers ")
    #if numbers == '':
    #    break
    numbers = int(numbers)
    print(type(numbers))
'''

def addNumbers(ns):
    #print(ns)
    #print(len(ns))
    sum = 0 # Sum is a Local Variable
    #[10,20,30,40] 
    for x in ns:
        #print(x)
        sum = sum + x

    print("The sum of array is {}".format(sum))




addNumbers(nums)


