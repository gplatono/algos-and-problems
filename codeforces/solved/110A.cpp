#include <iostream>
using namespace std;

int isLucky(int N) {
    if (N == 0)
        return 0;
    while (N > 0) {
        if (N % 10 != 7 && N % 10 != 4)
            return 0;
        N /= 10;
    }
    return 1;
}

int main() {
    unsigned long long N;
    cin >> N;
    int count = 0;
    while (N > 0) {
        if(N % 10 == 4 || N % 10  == 7)
            count++;
        N /= 10;        
    }
    if (isLucky(count)) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    return 0;
}