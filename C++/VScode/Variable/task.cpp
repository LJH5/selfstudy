#include <iostream>
using namespace std;

int main()
{
    int x = 1;
    x = x + 2;
    cout << x << "\n";      // #1

    int y = x;
    cout << y << "\n";      // #2

    cout << x + y << "\n";  // #3

    cout << x << "\n";      // #4

    int z;
    cout << z << "\n";      // #5

    return 0;
}