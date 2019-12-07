#include <iostream>

using namespace std;

int main()
{
    int a = 10;
    int* pA = &a;
    //int* pA = addressof(a);
    *pA = 20;
    cout << "a is " << a << endl;
    cout << "*pA is " << *pA << endl;
    cout << "pA is " << pA << endl;
}