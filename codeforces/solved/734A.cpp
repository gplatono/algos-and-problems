#include <iostream>
#include <string>
using namespace std;

int main(int argc, char** argv) {
    int n;
    string games;
    int anton_count = 0;
    cin >> n >> games;
    for (int i = 0; i < games.length(); i++) {
        if (games[i] == 'A')
            anton_count++;
    }
    if (2 * anton_count > games.length())
        cout << "Anton";
    else if (2 * anton_count < games.length()) 
        cout << "Danik";
    else 
        cout << "Friendship";
    return 0;
}