// C++20 이전 버전 import <iostream>; 
#include <iostream>
#include <format>

using namespace std;

void main()
{
	// 입력
	int value;
	cin >> value;
	int num;
	scanf("%d", &num); // C에서 사용하는 방식 C++에서도 지원,  cin보다 속도가 빠르지만 안정성이 낮음

	// 출력
	cout << "Hello, World!" << endl;	// 위에 std를 선언해서 'std::'를 붙이지 않아도 됨  
	cout << "Hello, World!" << "\n";		// endl과 \n의 기능은 유사함
	std::cout << "There are " << value << " ways, I love you." << std::endl;	// 옛날 방법	
	std::cout << std::format("There are {} ways, I love you.", value) << std::endl; //C++20 버전
	printf("%d", &num); // C에서 사용하는 방식 C++에서도 지원,  cout보다 속도가 빠르지만 안정성이 낮음
}