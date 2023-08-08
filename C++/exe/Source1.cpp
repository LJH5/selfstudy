#include <iostream>

using namespace std;

// 함수의 파라미터로 배열 넣기
void doSomething(int students_scores[20]) // <-- 얘는 문법상 포인터, 배열이 아니다!!!!!!!!!
{
	cout << &students_scores << endl;     // 0x61fdb0 다른 이유는 배열의 포인터 주소를 저장한 포인터 주소를 가져오기 때문
	cout << &students_scores[0] << endl;  // 0x61fd90 가르키고 있는 주소의 첫번째 값을 가져오면 동일함, 배열의 포인터 주소를 가져옴
	cout << students_scores[0] << endl;
	cout << students_scores[1] << endl;
	cout << students_scores[2] << endl;
}

int main()
{
	const int num_students = 20;

	int students_scores[num_students] = { 1, 2, 3, 4, 5 };  // 배열은 주소

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