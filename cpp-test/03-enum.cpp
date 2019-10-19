#include <iostream>

using namespace std;

int main()
{
    enum class choice1 { STONE, SCISSORS, PAPER };
    choice1 x = choice1::PAPER;
    cout << (x == choice1::STONE ? "STONE" : "not STONE") << endl;
}