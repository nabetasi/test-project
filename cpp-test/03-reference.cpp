#include <iostream>

using namespace std;

int main()
{
    int a = 10;
    int& b = a;
    int &c = a;
    b = 15;
    c = 22;
    cout << "a is " << a << endl;
    cout << "b is " << b << endl;
    cout << "c is " << c << endl;
}