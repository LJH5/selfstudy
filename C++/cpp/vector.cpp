#include <iostream>
#include <vector>

using namespace std;

void func(vector<int>& v) {
	v[4] = 10;
	v.push_back(7);	// vector의 맨 뒤에  값 추가
}

int main(void) {
	vector<int> v(10);
	func(v);
	cout << v.size() << "\n";
	cout << v.back();	// vector의 마지막 요소 출력

	return 0;
}