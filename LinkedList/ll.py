class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
n1=Node(100)
n2=Node(200)
n3=Node(300)
print(n1)
n1.next=n2
n2.next=n3

n4=Node(400)
n4.next=n1
current=n4
while current!=None:
    print(current.data)
    current=current.next