#Instead of putting everything in a single file, 
# we can use modules to separate codes in separate files as per their functionality.
#  This makes our code organized and easier to maintain.
#Module is a file that contains code to perform a specific task.
#  A module may contain variables, functions, classes etc
#we have created a module arithmeticop with the help of impport keyword we can use the module in another file.
from ArithmaticOp import *
ans= add(3,4)
print(ans)