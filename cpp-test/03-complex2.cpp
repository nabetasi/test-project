#include <iostream>
#include <complex>

using namespace std;

int main()
{
    using cplx = complex<double>;

    cplx* p = new cplx;

    cout << *p << endl;

    cplx* q = new cplx(3., 4.);

    cout << *q << endl;

    cplx* r = new cplx(*q);

    cout << *r << endl;

    cout << (*q).real() << endl;
    cout << (*q).imag() << endl;

    cout << q->real() << endl;
    cout << q->imag() << endl;

    delete p;
    delete q;
    delete r;

}