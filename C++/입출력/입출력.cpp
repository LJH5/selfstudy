// using namespace s// C++20 이전 버전 import <iostream>; 
#include <iostream>

using namespace std;

void main()
{
	// 입력
	int value;
	cin >> value;

	// 출력
	cout << "Hello, World!" << endl;	// 위에 std를 선언해서 'std::'를 붙이지 않아도 됨  
	cout << "Hello, World!" << "\n";		// endl과 \n의 기능은 유사함

	std::cout << "There are " << value << " ways, I love you." << std::endl;	// 옛날 방법	

	// std::cout << std::format("There are {} ways, I love you.", value) << std::endl; //C++20 버전
}