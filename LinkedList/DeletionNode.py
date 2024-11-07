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

#delete node at end
current=head
while current.next.next is not None:
    current=current.next
current.next=None

while head!=None:
    print(head.data)
    head=head.next