#include <iostream>
using namespace std;

int main() {
    int n, vote;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> vote;
        if (vote == 1) {
            cout << "HARD";
            return 0;            
        }
    }
    cout << "EASY";
    return 0;
}