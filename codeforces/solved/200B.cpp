#include <iostream>
using namespace std;

int main() {
    int n, p = 0, acc = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> p;
        acc += p;
    }
    printf("%.7f", (1.0 * acc) / n);
    return 0;
}