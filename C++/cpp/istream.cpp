#include <iostream>
#include <string>
#include <iomanip>	// 입출력 조작

using namespace std;

int main()
{
	char buf[5];					// char는 마지막 자리에 null pointer를 가짐, 실질적으로 4글자 입력됨

	// cin >> buf;			     	// 5자 이상 입력 받으면 런타임 오류 발생
	cin >> setw(5) >> buf;  // 최대 5개만 입력받음, 오류X
	cout << buf << endl;
	
	cin >> setw(5) >> buf;  
	cout << buf << endl;

	cin >> setw(5) >> buf;  
	cout << buf << endl;

	return 0;
}