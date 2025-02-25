#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char** argv)
{
    int n;
    char s[51];
    int rmv = 0;
    cin >> n;
    scanf("%s", &s);
    for (int i = 1; i < n; i++) {
        if (s[i] == s[i-1]) {
            rmv++;
        }
    }
    cout << rmv << endl;
    return 0;
} 