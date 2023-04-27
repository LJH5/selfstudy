#include <iostream>
#include <array>
#include <format>
using namespace std;

struct Point{ double m_a, m_b, m_c; };	// ����ü�� �⺻������ public

int main() {
	// ���� 1
	array values{ 11, 22, 33 };
	auto [x, y, z]{ values };
	cout << format("{} {} {} \n", x, y, z);
	
	// ����2, public���� ����� ����ü���� ���� ����
	Point point;
	point.m_a = 1.0; point.m_b = 2.0, point.m_c = 3.0;
	auto [a, b, c] { point };
	cout << format("a: {}, b: {}, c: {} \n", a, b, c);

	// ����3, pair�� �̿��ϱ�
	pair myPair{ "hello", 5 };
	auto [theString, theInt] { myPair };
	cout << format("theString: {} \n", theString);
	cout << format("theInt: {} \n", theInt);
}