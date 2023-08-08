#include <bits/stdc++.h>
using namespace std;

void cntNum(int result) {
	int arr[10] = { 0 };		// C++은 초기값이 0이 아니라 0 초기화 해줘야 함
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