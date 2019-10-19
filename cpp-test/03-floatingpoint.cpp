#include <iostream>
#include <cmath>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    double x = 0.1;
    double y = x + x + x + x + x + x + x + x + x + x;

    cout << (y == 1.) << endl;
    cout << y << endl;
    cout << setprecision(20);
    cout << "x is " << x << endl;
    cout << "y is " << y << endl;
    cout << hexfloat;
    cout << "x(hexfloat) is " << x << endl;
    cout << defaultfloat;

    double z = stod("0x1.999999999999ap-4");
    cout << (x == z ? "equal" : "not equal") << endl;

    double epsilon = 1e-10;
    cout << "check precision : " << (abs(y - 1.0) < epsilon ? "OK" : "NG") << endl;
}