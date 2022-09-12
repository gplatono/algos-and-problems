#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main(int argc, char** argv) {
    int n, x, y;
    cin >> n >> x >> y;
    if (abs(n/2 - x) == 1 && abs(n/2 - y) == 1)
        cout << "NO";
    else
        cout << "YES";
    return 0;
}