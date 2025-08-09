print("-----------------------------------------------------")
print("LOOPS")
print("-----------------------------------------------------")
print("SCENARIO 1: for loop")
nums=[1,2,3,4]
for num in nums:
    print(num)
print("-----------------------------------------------------")
print("SCENARIO 2: for loop -> break")
print("break -> Immediately exit the loop entirely, no matter if there are more iterations left.")
print("break -> Loop stops running.")
nums=[1,2,3,4]
for num in nums:
    if num ==3:
        print('Found!')
        break
    print(num)
print("-----------------------------------------------------")
print("SCENARIO 3: for loop -> continue")
print("continue -> Skip the rest of the code in the current iteration and go to the next iteration.")
print("continue -> Loop keeps running, just skips one turn.")
nums=[1,2,3,4]
for num in nums:
    if num ==3:
        continue
    print(num)
print("-----------------------------------------------------")
print("SCENARIO 4: for loop -> Loop within Loop")
for num in nums:
    for letter in 'abc':
        print(num, letter)
print("-----------------------------------------------------")
print("SCENARIO 5: for loop -> range(start,end-1)")
print ("start -> inclusive")
print("end -> is not inclusive")
for i in range(1,11):
    print(i)
print("-----------------------------------------------------")
print("SCENARIO 6: while loop")
x=0
while(x<10):
    print(x)
    x+=1
print("-----------------------------------------------------")
print("SCENARIO 7: while loop -> break")
x=0
while(x<10):
    if (x==5):
        print(x)
        x += 1
        break
print("-----------------------------------------------------")
