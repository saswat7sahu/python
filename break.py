#break allows you to exit a loop when an external condition is met.
a=10
i=0
while i==0:
    print(a)
    if(a==5):
        break
    a-=1
# When the continue statement is executed in the loop,
#  the code inside the loop following 
# the continue statement will be skipped and the next iteration of the loop will begin.
for i in range(101):
    if(i%10!=0):
        continue
    print(i)
# Pass the statement but keep in the iteration
for i in range(10):
    if(i%2==0):
        pass
    else:
        print(i)