#include <iostream>
#include <string>
using namespace std;

string processQueue(string queue) {
    for (int i = 0; i < queue.length() - 1; i++) {
        if (queue[i] == 'B' && queue[i+1] == 'G') {
            queue[i] = 'G';
            queue[i+1] = 'B';
            i++;
        }
    }
    return queue;    
}

int main() {
    int n, t;
    string queue;
    cin >> n >> t >> queue;
    for (int i = 0; i < t; i++)
        queue = processQueue(queue);
    cout << queue;
    return 0;
}