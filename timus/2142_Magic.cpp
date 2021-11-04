#include <iostream>
using namespace std;

int main(int argc, char** argv) 
{
    long long A, B, C;
    long long rA, rB, rO;
	cin >> A >> B >> C >> rA >> rB >> rO;
    A -= rA;
    B -= rB;
    if (C + A >= 0 && C + B >= 0 && C + A + B >= 0 && A + B + C >= rO)
        cout << "It is a kind of magic";
    else
        cout << "There are no miracles in life";
    return 0;
}