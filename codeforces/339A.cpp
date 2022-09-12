#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

string append(string in, int count, char symb)  {
    while (count > 0) {
        in += symb;
        in += "+";
        count--;
    }
    return in;
}

int main(int argc, char** argv) {
    char s[101];
    cin >> s;
    int ones = 0, twos = 0, threes = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == '1')
            ones++;
        else if (s[i] == '2')
            twos++;
        else if (s[i] == '3')
            threes++;
    }   
    
    string out = append(append(append("", ones, '1'), twos, '2'), threes, '3');
    out.pop_back();

    cout << out << endl;

    return 0;    
}