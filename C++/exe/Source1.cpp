#include <iostream>

using namespace std;

// �Լ��� �Ķ���ͷ� �迭 �ֱ�
void doSomething(int students_scores[20]) // <-- ��� ������ ������, �迭�� �ƴϴ�!!!!!!!!!
{
	cout << &students_scores << endl;     // 0x61fdb0 �ٸ� ������ �迭�� ������ �ּҸ� ������ ������ �ּҸ� �������� ����
	cout << &students_scores[0] << endl;  // 0x61fd90 ����Ű�� �ִ� �ּ��� ù��° ���� �������� ������, �迭�� ������ �ּҸ� ������
	cout << students_scores[0] << endl;
	cout << students_scores[1] << endl;
	cout << students_scores[2] << endl;
}

int main()
{
	const int num_students = 20;

	int students_scores[num_students] = { 1, 2, 3, 4, 5 };  // �迭�� �ּ�

	cout << students_scores << endl;			  // 0x61fd90
	cout << &students_scores << endl;			  // 0x61fd90
	cout << (int)students_scores << endl;		  // 5240520
	cout << (int)&students_scores << endl;     // 5240520   
	cout << students_scores[0] << endl;
	cout << students_scores[1] << endl;
	cout << students_scores[2] << endl;

	doSomething(students_scores);

	return 0;
}