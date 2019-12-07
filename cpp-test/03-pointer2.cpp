#include <iostream>

using namespace std;

int main()
{
    int a = 10;
    int* pA = &a;
    int** ppA = &pA;
    cout << **ppA << endl;
}