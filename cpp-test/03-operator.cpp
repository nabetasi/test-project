#include <iostream>

using namespace std;

int main()
{
    int h = 0;
    int m = 0;
    h = static_cast<int>(1.0);
    cout << h << endl;
    cout << (2 > 1 ? "ABC" : "DEF") << endl;
    cout << (m=1, m+2) << endl;
}