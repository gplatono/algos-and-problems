#include <iostream>
#include <string>
using namespace std;

int main() {
    string h = "hello", s;
    int i = 0, j = 0;
    cin >> s;
    while (i < 5 && j < s.length()) {
        if (s[j] == h[i]) {
            i++;
        }
        j++;
    }
    if (i == 5) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    return 0;
}