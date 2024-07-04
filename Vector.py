class Vector:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    def __add__(self,another):
        return self.x+another.x,self.y+another.y
v1=Vector(2,3)
v2=Vector(5,3)
res=v1+v2
print(res)