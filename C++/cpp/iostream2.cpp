#include <iostream>
#include <iomanip>	// 입출력 조작

using namespace std;

int main()
{
	cout.setf(ios::showpos);	b					// 부호 표시하기
		cout << 108 << endl;

	cout.unsetf(ios::showpos);					// 부호 표시 안 하기
	cout << 108 << endl;

	//cout.setf(ios::hex, ios::basefield);		// 16진수로 표현하기
	cout << hex;								        // 16진수로 표현하기2
	cout << 108 << endl;

	cout << dec;										// 10진수로 표현하기
	cout << 108 << endl;

	cout.setf(ios::uppercase);					// 소문자를 대문자로 표현
	cout << hex << 108 << endl;

	cout << boolalpha;								// true, false를 문자열 로 출력
	cout << true << " " << false << endl;

	cout << setprecision(3) << 123.456 << endl;	// 총 자릿수 표현. 반올림
	cout << setprecision(4) << 123.456 << endl;
	cout << setprecision(5) << 123.456 << endl;
	cout << setprecision(6) << 123.456 << endl;

	cout << fixed;	// 소숫점 아래 자릿수 표현
	cout << setprecision(3) << 123.456 << endl;
	cout << setprecision(4) << 123.456 << endl;
	cout << setprecision(5) << 123.456 << endl;
	cout << setprecision(6) << 123.456 << endl;

	cout << scientific;	// 지수 표기법
	cout << setprecision(3) << 123.456 << endl;
	cout << setprecision(4) << 123.456 << endl;
	cout << setprecision(5) << 123.456 << endl;
	cout << setprecision(6) << 123.456 << endl;

	return 0;
}