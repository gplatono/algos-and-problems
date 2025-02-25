#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char** argv) {
    char s[1001];
    cin >> s;
    if (s[0] > 90)
        s[0] -= 32;
    cout << s << endl;
    return 0;
}