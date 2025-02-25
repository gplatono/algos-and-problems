#include <iostream>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    while (M > 0) {
        int last_digit = N % 10;        
        if (last_digit >= M) {
            N -= M;
            M = 0;
        }
        else {
            M -= (last_digit + 1);
            N /= 10;
        }

    }
    cout << N;
    return 0;
}