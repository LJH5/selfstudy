#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    // 문자 배열
    char myString[] = "string"; 
    
    // 배열은 크기는 7, string 뒤에 \0(널 캐릭터) 생략되어있음
    // 널 캐릭터는 문자열이 끝남을 알려주는 역할을 함
    // cout이 \0를 만나면 출력을 종료함
    
    for (int i = 0; i < 7; i++)
    {
        cout << (int)myString[i] << endl; // 6번 인덱스에 0이 있음을 볼 수 있음
    }

    cout << sizeof(myString) / sizeof(myString[0]) << endl;

    char myString2[255];
    cin.getline(myString2, 255);    // getline을 사용해야 띄어쓰기도 입력됨
    cout << myString2 << endl;

    // C 스타일 코딩: cstring
    char source[] = "Copy this!";
    char dest[50];
    strcpy(dest, source);

    cout << source << endl;
    cout << dest << endl;

    return 0;
}