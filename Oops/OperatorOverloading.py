#It refers to the ability of a function or an operator to behave in different ways depending on the parameters 
# that are passed to the function, or the operands that the operator acts on.
class vector:
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def __add_(self,other):
        return vector(other.x+self.x,other.y+self.y)
    