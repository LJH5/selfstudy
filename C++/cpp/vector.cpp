#include <iostream>
#include <vector>

using namespace std;

void func(vector<int>& v) {
	v[4] = 10;
	v.push_back(7);	// vector�� �� �ڿ�  �� �߰�
}

int main(void) {
	vector<int> v(10);
	func(v);
	cout << v.size() << "\n";
	cout << v.back();	// vector�� ������ ��� ���

	return 0;
}