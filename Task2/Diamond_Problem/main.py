class A:
    def __init__(self) -> None:
        print("A", end="")

class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("B", end="")

class C(A):
    def __init__(self) -> None:
        super().__init__()
        print("C", end="")

class D(C, B):
    def __init__(self) -> None:
        super().__init__()
        print("D", end="")

D()
