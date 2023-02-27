#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char** argv) {
    int val;
    int x, y;
    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++) {
            cin >> val;
            if (val == 1) {
                x = i+1;
                y = j+1;
            }
        }
    cout << abs(x-3) + abs(y-3) << endl;
    return 0;
}