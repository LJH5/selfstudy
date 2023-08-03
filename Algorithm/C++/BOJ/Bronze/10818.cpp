#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	int max = -1000000;
	int min = 1000000;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		if (num > max) {
			max = num;
		}
		if (num < min) {
			min = num;
		}
	}
	cout << min << " " << max;

	return 0;
}