#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int year;
	cin >> year;

	// ������ 4�� ����̸鼭 100�� ����� �ƴҶ� �Ǵ� 400�� ����϶�
	if (year % 400 == 0) {
		cout << 1 << "\n";
	}
	else if (year % 4 == 0 and year % 100 != 0) {
		cout << 1 << "\n";
	}
	else {
		cout << 0 << "\n";
	}

	return 0;
}