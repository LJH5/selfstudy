#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cout << "1���� �迭 \n";
	int arr[5] = { 1, 2, 3, 4, 5 };
	for (auto i : arr) {
		cout << i << " ";
	}
	cout << "\n\n";

	cout << "2���� �迭 \n";
	int matrix[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
	for (const auto& row : matrix) {
		for (const auto& col : row) {
			cout << col << " ";
		}
		cout << "\n";
	}

	// ���1 memset

	return 0;
}