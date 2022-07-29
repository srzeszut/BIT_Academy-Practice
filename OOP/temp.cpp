#include <iostream>

class node
{
private:
    int x;
protected:
    int y;
public:
    int z;
    node(int a, int b, int c)
    {
        x = a;
        y = b;
        z = c;
    }
};

int main()
{
    node A(1, 2, 3);
    std::cout << A.z;
}