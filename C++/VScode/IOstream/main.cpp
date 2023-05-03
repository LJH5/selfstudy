#include <iostream>  // cout, cin, endl, ...
#include <cstdio>    // printf

int main()
{
    int x = 1024;
    
    // 출력
    std::cout << "I love ";
    std::cout << "x is " << x << std::endl;
    
    std::cout << "abc" << "\t" << "def" << std::endl;
    std::cout << "abc \n\n\n" << "where \n";

    using namespace std;
    cout << "편하다";
    cout << "\a";

    printf("I love \n");

    // 입력
    int y;

    cout << "정수를 입력하세요: ";
    cin >> y;
    cout << "Your input is " << y << endl;

    return 0;
}