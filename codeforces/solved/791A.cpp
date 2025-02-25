#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char** argv) {
    int a, b;
    cin >> a >> b;
    cout << floor(1 + log((double)b/a) / log(1.5)) << endl;
    return 0;
}