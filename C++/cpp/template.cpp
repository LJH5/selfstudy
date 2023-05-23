#include <iostream>

using namespace std;

template<typename T>                        // 템플릿 선언

T getMax(T x, T y)                          // 템플릿으로 타입을 처리
{
    return (x > y) ? x : y;
}

int main()
{
    cout << getMax(1 , 2) << endl;          // 정수형
    cout << getMax(3.14, 1.592) << endl;    // 실수형
    cout << getMax("a", "b") << endl;       // 문자형
    
    return 0;
}