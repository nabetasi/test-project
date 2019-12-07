#include <iostream>
using namespace std;

int main() {
    int n, divisors;

    n = 10;
    divisors = 0;
    for (int i = 1; i <= n; ++i) {
        if ( n % i == 0) ++divisors;
    }
    cout << n << " divisors num:" << divisors << endl;

    n = 12;
    divisors = 0;
    for (int i = 1; i <= n; ++i) {
        if (n % i == 0) ++divisors;
    }
    cout << n << " divisors num:" << divisors << endl;
}