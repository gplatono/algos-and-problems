#include <iostream>
using namespace std;

int main(int argc, char** argv) 
{
    int n;
    int val = 0;
    char op[4];
    cin >> n;
    for (int i = 0; i < n; i++) 
    {
        scanf("%s", &op);
        for (int j = 0; j < 3; j++)
            if (op[j] == '+') {
                val++;
                break;
            }
            else if(op[j] == '-') {
                val--;
                break;
            }
    }
    cout << val << endl;
    return 0;
}