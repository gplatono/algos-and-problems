#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char** argv) {
    char input[101];
    cin >> input;
    int lower = 0;
    int upper = 0;
    for (int i = 0; i < strlen(input); i++) {
        if ((int)input[i] >= 65 && (int)input[i] <= 90) {
            upper++;
            input[i] = (char)(input[i] + 32);
        }
        else 
            lower++;
    }
    if (lower >= upper) {
        cout << input;
        return 0;
    }
    for (int i = 0; i < strlen(input); i++) {
        cout << (char)(input[i] - 32);
    }
    return 0;
}