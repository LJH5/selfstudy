#include <iostream>

using namespace std;

// 구조체에서 배열 사용하기
struct Rectengle
{
    int length;
    int width;
};

int main() {
    cout << sizeof(Rectengle) << endl;

    Rectengle rect_arr[10];

    cout << sizeof(rect_arr) << endl;

    rect_arr[0].length = 1;
    rect_arr[0].width = 2;


}