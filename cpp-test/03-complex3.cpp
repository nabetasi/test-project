#include <iostream>
#include <complex>
#include <memory>

using namespace std;

int main()
{
    using cplx = complex<double>;

    shared_ptr<cplx> p = make_shared<cplx>();

    cout << *p << endl;

    shared_ptr<cplx> q = make_shared<cplx>(3., 4.);
    cout << *q << endl;
    
    shared_ptr<cplx> r = make_shared<cplx>(*q);
    cout << *r << endl;
}