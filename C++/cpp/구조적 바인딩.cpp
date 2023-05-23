#include <iostream>
#include <array>
#include <format>
using namespace std;

struct Point{ double m_a, m_b, m_c; };	// 구조체는 기본적으로 public

int main() {
	// 예제 1
	array values{ 11, 22, 33 };
	auto [x, y, z]{ values };
	cout << format("{} {} {} \n", x, y, z);
	
	// 예제2, public으로 선언된 구조체에도 적용 가능
	Point point;
	point.m_a = 1.0; point.m_b = 2.0, point.m_c = 3.0;
	auto [a, b, c] { point };
	cout << format("a: {}, b: {}, c: {} \n", a, b, c);

	// 예제3, pair를 이용하기
	pair myPair{ "hello", 5 };
	auto [theString, theInt] { myPair };
	cout << format("theString: {} \n", theString);
	cout << format("theInt: {} \n", theInt);
}