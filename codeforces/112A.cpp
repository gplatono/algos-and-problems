#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char** argv) {
    char fs[101];
    char ss[101];
    int cmp = 0;
    cin >> fs >> ss;
    for (int i = 0; i < strlen(fs); i++) {
        if (fs[i] > 90)
            fs[i] -= 32;
        if (ss[i] > 90)
            ss[i] -= 32;
        if (fs[i] - ss[i] > 0) {
            cmp = 1;
            break;
        }
        else if(fs[i] - ss[i] < 0) {
            cmp = -1;
            break;
        }
    }
    cout << cmp << endl;
    return 0;
}