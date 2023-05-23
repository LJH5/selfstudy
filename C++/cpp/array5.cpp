#include <iostream>

using namespace std;

int main()
{
  const int num_students = 20;

  int students_scores[num_students];

  // 배열의 메모리 주소 확인 -> 4씩 증가
  cout << &students_scores << endl;     // 0x61fdc0 
  cout << &students_scores[0] << endl;  // 0x61fdc0 
  cout << &students_scores[1] << endl;  // 0x61fdc4 
  cout << &students_scores[2] << endl;  // 0x61fdc8 
  cout << &students_scores[3] << endl;  // 0x61fdcc 

  cout << sizeof(students_scores) << endl;

  return 0;
}