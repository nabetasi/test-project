#include <iostream>
#include <string>
#include <complex>

using namespace std;

int main()
{
    cout << "\"(^_^)\"" << endl;
    cout << R"XXX("(^_^)")XXX" << endl;

    auto a = (unsigned)1 + (int)-2;
    cout << a << endl;

    complex<double>* p = new complex<double>(5., 10.);
    cout << abs(*p) << endl;
    delete p;
}