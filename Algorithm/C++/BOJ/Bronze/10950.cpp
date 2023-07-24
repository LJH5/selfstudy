#include <bits/stdc++.h>
using namespace std;

int mySum(int a, int b) {
	return a + b;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int a, b;
		cin >> a >> b;
		int result = mySum(a, b);
		cout << result << "\n";
	}

	return 0;
}