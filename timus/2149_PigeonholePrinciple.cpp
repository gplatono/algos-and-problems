#import <iostream>
#import <string>
using namespace std;

int main(int argc, char** argv)
{
    int n;
    int in = 0, out = 0, odd_left = 0, odd_right = 0;
    string a, b, c;
    cin >> n >> a >> b >> c;
    int half = a.length() / 2;    
    for (int i = 0; i < a.length(); i += 5)
    {
        if (a[i] == '<') 
        {
            if (i <= half) 
                in++;
            else
                out++;
            if (!(i & 1))
                odd_right++;
            else
                odd_left++;
        }
        else
        {
            if (i <= half) 
                out++;
            else
                in++;
            if (!(i & 1))
                odd_left++;
            else
                odd_right++;
        }                
    }
    cout << min(min(in, out), min(odd_right, odd_left)) << endl;
    return 0;
}