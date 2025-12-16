#include <iostream>
using namespace std;

int isBeautiful(int num) {
    if (num == 0)
        return 0;
    while (num > 0) {
        if (num % 10 != 4 && num % 10 != 7)
            return 0;
        num /= 10;
    }
    return 1;
}

int main() {
    int n, flags[1000];
    cin >> n;
    for (int i = 1; i <= 1000; i++)
        flags[i-1] = isBeautiful(i);
    for (int i = 1; i <= n; i++)
        if (n % i == 0 && flags[i-1] == 1) {
            cout << "YES";
            return 0;
        }
    cout << "NO";
    return 0;
}