class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
n1=Node(100)
n2=Node(200)
n3=Node(300)
n4=Node(400)
n5=Node(500)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
head=n1
current=head
newnode=Node(6666)
while current.next is not None and current.data!=300:
    current=current.next
newnode.next=current.next
current.next=newnode
