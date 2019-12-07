#include <iostream>
using namespace std;

void mySwap(int& a, int& b)
{
    int tmp = a;
    a = b;
    b = tmp;
    cout << "int swap" << endl;
}

void mySwap(double& a, double& b)
{
    double tmp = a;
    a = b;
    b = tmp;
    cout << "double swap" << endl;
}

int main()
{
    int a = 1;
    int b = 2;
    mySwap(a, b);
    cout << a << endl;
    cout << b << endl;

    double x = 1.23;
    double y = 4.56;
    mySwap(x, y);
    cout << x << endl;
    cout << y << endl;
}