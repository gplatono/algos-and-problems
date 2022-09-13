#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

string num_to_num(string num, int from_base, int to_base, int from_offset, int to_offset) {
    int n = 0;
    for (int i = 0; i < num.length(); i++) {
        n = n*from_base + (num[i] - from_offset);
    }
    //cout << "N = " << n << endl;
    string result = "";
    while (n > 0) {
        int digit = n % to_base;
        if (to_base == 26 && digit == 0)
            digit = 26;
        n -= digit;
        n /= to_base;
        string tmp = "";
        tmp += (char)(digit + to_offset);
        //cout << " TMP = " << tmp << " " << n << endl;
        result = tmp + result;
    }
    return result;
}

int main(int argc, char** argv) {

    int n;
    string input;
    string row, col;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> input;
        row = "";
        col = "";
        int state = input[0] == 'R'? 1 : 0;
        for (int i = 1; i < input.length(); i++) {
            if (state == 1 && input[i] <= '9')
                state = 2;
            if (state == 2 && input[i] == 'C') {
                state = 3;
                break;
            }
        }

        if (state != 3) {
            int j = 0;
            for (; input[j] >= 'A'; j++)
                col += input[j];
            row = input.substr(j);
            col = num_to_num(col, 26, 10, 64, 48);
            cout << "R" << row << "C" << col << endl;
        }
        else {
            int j = 1;
            for (; input[j] != 'C'; j++) {
                row += input[j];
            }
            col = input.substr(j+1);
            col = num_to_num(col, 10, 26, 48, 64);
            cout << col << row << endl;
        }
    }
    return 0;
}