#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, count = 0, last;
    string mag, prev_mag;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> mag;        
        if (count == 0 || mag[0] == prev_mag[1])
            count++;
        prev_mag = mag;
    }
    cout << count;
    return 0;
}