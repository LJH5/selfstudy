#include <iostream>

using namespace std;

int a;							// a 선언, 초기값은 0
//a = 7;						// 이렇게 하면 a에 값 할당 안 됨 
// int a {};				    // 변수 재정의 안 됨
int b = 7;
int c { 7 };					// 균일 초기화
unsigned int d = 7;		// unsigned는 범위를 0 이상으로 제한, 대신 더 넓은 범위의 양수 값 할당 가능
unsigned int e = -7;	// 변수가 선언되었으나 음수값이 할당되지 못해 주소값을 반환
long long f = 7;			// 주로 8바이트로  큰 범위의 변수를 할당

float myFloat{ 3.14f };					// 형변환
int i1 { (int)myFloat };						// 방법 1 (권장 안 함)
int i2 { int(myFloat) };						// 방법 2 (거의 사용 안 함)
int i3{ static_cast<int>(myFloat) };  // 방법 3 (권장)

int main() {
	cout << "a:" << a << "\n";
	cout << "b:" << b << "\n";
	cout << "c:" << c << "\n";
	cout << "d:" << d << "\n";
	cout << "e:" << e << "\n";
}