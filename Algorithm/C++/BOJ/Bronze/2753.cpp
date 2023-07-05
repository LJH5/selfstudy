#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int year;
	cin >> year;

	// 윤년은 4의 배수이면서 100의 배수가 아닐때 또는 400의 배수일때
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