#include <iostream>
using namespace std;

int main() {
    int n, a, b, capacity = 0, needed_capacity = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        capacity += b - a;
        if (capacity > needed_capacity) {
            needed_capacity = capacity;
        }
    }
    cout << needed_capacity;
    return 0;
}