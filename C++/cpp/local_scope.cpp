#include <iostream>

using namespace std;

int main()
{   
    int x(0); // x = 0;
    cout << x << " " << &x << endl;     // 0 0x7fffc77603a0
    {
        int x = 1;
        cout << x << " " << &x << endl; // 1 0x7fffc77603a4
    }
    {
        int x = 2;
        cout << x << " " << &x << endl; // 2 0x7fffc77603a4
    }
    {
        x = 1;
        cout << x << " " << &x << endl; // 1 0x7fffc77603a0
    }
    cout << x << " " << &x << endl;     // 1 0x7fffc77603a0
    // 1과 2의 메모리 주소가 같은 이유는 
    // 1이 영역을 벗어나면서 스텍 메모리로 반납을 하고
    // 2가 반납된 메모리를 차지하였기 때문이다
    return 0;
}