#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char** argv) {
    int n, x, y, z, xt = 0, yt = 0, zt = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x >> y >> z;
        xt += x;
        yt += y;
        zt += z;
    }
    if (xt == 0 && yt == 0 && zt == 0)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}