#include <iostream>

using namespace std;

int a;							// a ����, �ʱⰪ�� 0
//a = 7;						// �̷��� �ϸ� a�� �� �Ҵ� �� �� 
// int a {};				    // ���� ������ �� ��
int b = 7;
int c { 7 };					// ���� �ʱ�ȭ
unsigned int d = 7;		// unsigned�� ������ 0 �̻����� ����, ��� �� ���� ������ ��� �� �Ҵ� ����
unsigned int e = -7;	// ������ ����Ǿ����� �������� �Ҵ���� ���� �ּҰ��� ��ȯ
long long f = 7;			// �ַ� 8����Ʈ��  ū ������ ������ �Ҵ�

float myFloat{ 3.14f };					// ����ȯ
int i1 { (int)myFloat };						// ��� 1 (���� �� ��)
int i2 { int(myFloat) };						// ��� 2 (���� ��� �� ��)
int i3{ static_cast<int>(myFloat) };  // ��� 3 (����)

int main() {
	cout << "a:" << a << "\n";
	cout << "b:" << b << "\n";
	cout << "c:" << c << "\n";
	cout << "d:" << d << "\n";
	cout << "e:" << e << "\n";
}