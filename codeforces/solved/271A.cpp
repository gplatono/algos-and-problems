#include <iostream>
using namespace std;

bool isBeautiful(int year) {
    int first = year % 10;
    int second = (year / 10) % 10;
    int third = (year / 100) % 10;
    int fourth = (year / 1000);
    return (first - second) * (first - third) * (first - fourth) * (second - third) * (second - fourth) * (third - fourth) != 0;
}

int main() {
    int n, m;
    cin >> n;
    for (m = n+1; m < 10000; m++)
        if(isBeautiful(m))
            break;
    cout << m;
    return 0;
}