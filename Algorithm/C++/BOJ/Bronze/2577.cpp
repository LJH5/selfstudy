#include <bits/stdc++.h>
using namespace std;

void cntNum(int result) {
	int arr[10] = { 0 };		// C++�� �ʱⰪ�� 0�� �ƴ϶� 0 �ʱ�ȭ ����� ��
	while (result > 10) {
		int num = result % 10;
		result /= 10;
		arr[num] += 1;
		//cout << num << " " << result << "\n";
	}
	arr[result] += 1;

	for (auto i : arr) {
		cout << i << "\n";
	}
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int result = 1;
	for (int i = 0; i < 3; i++) {
		int num;
		cin >> num;
		result *= num;
	}
	cntNum(result);

	return 0;
}