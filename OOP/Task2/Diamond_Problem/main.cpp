#include <iostream>
#include <string.h>

class A
{
public:
    A(){std::cout << "A";}
};

class B: public A
{
public:
    B(): A(){std::cout << "B";}
};

class C: public A
{
public:
    C(): A(){std::cout << "C";}
};

class D: public B, public C
{
public:
    D(): B(), C(){std::cout << "D";}
};

int main()
{
    D y;
}

int x()
{
    return "S";
}