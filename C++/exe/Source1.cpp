#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	vector<int> v1(3, 5);			// {5, 5, 5};
	cout << v1.size() << "\n";	// 3
	v1.push_back(7);				// {5, 5, 5, 7};
	
	vector<vector<int>> v2 = { {1, 2, 3}, {4, 5, 6} };
	for (const auto row : v2) {
		for (const auto col : row) {
			cout << col << " ";
		}
		cout << "\n";
	}

	return 0;
}