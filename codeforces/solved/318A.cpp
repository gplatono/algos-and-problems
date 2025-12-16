#include <iostream>
using namespace std;

int main() {
    long long n, k, even, odd;
    cin >> n >> k;
    even = n >> 1;
    odd = n - even;
    if (k <= odd)
        cout << 2*k - 1;
    else cout << (k - odd) * 2;
    return 0;
}