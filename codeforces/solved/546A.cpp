#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char** argv) {
    int k, n, w;
    cin >> k >> n >> w;
    int tot_cost = k*w*(w+1)/2;
    if (n < tot_cost)
        cout << tot_cost - n << endl;
    else 
        cout << 0 << endl;
    return 0;
}