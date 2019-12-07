#include <iostream>
#include <complex>

using namespace std;

int main()
{
    using cplx = complex<double>;

    cplx a;

    cout << a << endl;

    cplx b(3., 4.);

    cout << b << endl;

    cplx c(b);
    cout << c << endl;

    cplx d;
    d = b;
    cout << d << endl;

    cout << b.real() << endl;
    cout << b.imag() << endl;
}