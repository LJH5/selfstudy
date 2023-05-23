#include <iostream>
#include <string>
#include <iomanip>	// 입출력 조작

using namespace std;

int main()
{
	// 1
	int i;
	float f;

	cin >> i >> f;
	cout << i << " " << f << endl;

	// 2
	char ch;

	// while (cin >> ch)	// 공백이 사라지는 아쉬움이 있음
	while (cin.get(ch))
		cout << ch;
	
	// 3
	char buf[10];
	
	cin.get(buf, 3);							// .get을 사용하면 공백을 그대로 출력
	cout << cin.gcount() << endl;		// 입력받은 글자수 출력
	cout << buf << endl;

	cin.get(buf, 5);
	cout << buf << endl;

	// 4
	cin.getline(buf, 5);
	cout << buf << endl;

	// 5
	char buf2[5];
	cin.get(buf2, 2);
	cout << buf2 << endl;
	cin.putback('A');	// 버퍼 맨 앞에 추가
	cin >> buf2;
	cout << buf2 << endl;

	return 0;
}