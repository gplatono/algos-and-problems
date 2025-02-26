#include <iostream>
using namespace std;

int main() {
    int n, a, even_idx = -1, odd_idx = -1;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a;
        if ((a & 1) == 0) {
            if (even_idx == -1) {                
                even_idx = i;
            }
            else {
                even_idx = 1000000;
            }
        }
        else {
            if (odd_idx == -1) {
                odd_idx = i;
            }
            else {
                odd_idx = 1000000;
            }
        }
    }
    if (even_idx > -1 && even_idx < 1000000) {
        cout << even_idx;
    }
    else {
        cout << odd_idx;
    }
    return 0;    
}