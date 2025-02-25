#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main(int argc, char** argv) {
    int n, x, y;
    cin >> n >> x >> y;
    n /= 2;
    if (n <= x && x <= n+1 && n <= y && y <= n+1)
        cout << "NO";
    else
        cout << "YES";
    return 0;
}