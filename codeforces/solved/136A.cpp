#include <iostream>
using namespace std;

int main() {
    int n, g;
    cin >> n;
    int giftees[n];
    for (int i = 0; i < n; i++) {
        cin >> g;
        giftees[g-1] = i + 1;
    }
    for (int i = 0; i < n; i++) {
        cout << giftees[i];
        if (i != n - 1) 
            cout << " ";
    }
    return 0;
}