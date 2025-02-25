#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char** argv) {
    int t, n, m, x, y;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n >> m;
        for (int j = 0; j < m; j++) {
            cin >> x >> y;
        }
        if (m < n)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}