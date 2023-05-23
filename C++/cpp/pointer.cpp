#include <iostream>
#include <typeinfo>

using namespace std;

int* def(int* ptr_a)    // 함수에도 포인터 사용 가능
{
    return nullptr;
}

int main()
{
    int x = 5;

    cout << x << endl;
    cout << &x << endl;     // &: adress-of operator. 메모리 주소를 가르킴
    cout << *&x << endl;    // *: de-reference operator, 메모리 주소에 저장된 값을 가르킴
    
    // 포인터
    int *ptr_x = &x;

    cout << ptr_x << endl;  // 주소를 가르킴
    cout << *ptr_x << endl; // 주소에 저장된 값을 가르킴
    cout << typeid(ptr_x).name() << endl;

    return 0;
}