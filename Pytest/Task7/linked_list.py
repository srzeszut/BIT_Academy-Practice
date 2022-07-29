class node:
    def __init__(self, val = None):
        self.val  = val
        self.next = None

A = node(3)
B = node(4)
C = node(7)
D = node(2)
A.next = B
B.next = C
C.next = D
head = A

tab = []
while head:
    print(head, head.val)
    tab.append(head.val)
    head = head.next

print(tab)
tab.sort()

A = node(tab[0])
B = node(tab[1])
C = node(tab[2])
D = node(tab[3])
A.next = B
B.next = C
C.next = D
head = A

tab = []
while head:
    print(head, head.val)
    tab.append(head.val)
    head = head.next


