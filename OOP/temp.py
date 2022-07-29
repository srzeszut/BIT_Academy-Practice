# klasy
class node:
# konstruktory
    def __init__(self, val, nex = None):
        self.val = val
        self.next = nex

# pola, metody
    def __add__(self, other):
        if not self.next:
            self.next = other
        else:
            self.next + other
        return self

# public, protected, private

# static
    tab = [1, 2, 3]

print(node.tab)


class vector:
    def add(A, B):
        output = [A[i] + B[i] for i in range(len(A))]
        return output

    def sub(A, B):
        pass

print(vector.add([1, 2, 3], [2, 4, 2]))