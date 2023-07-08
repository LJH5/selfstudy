#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int arr[5] = { 1, 2, 3, 4, 5 };
	int matrix[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
	
	// memset
	memset(arr, 0, sizeof arr);
	memset(matrix, 0, sizeof matrix);

	// for
	for (int i = 0; i < 5; i++)
		arr[i] = 0;
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			matrix[i][j] = 0;

	// fill
	fill(arr, arr + 5, 0);
	for (int i = 0; i < 3; i++)
		fill(matrix[i], matrix[i] + 3, 0);
	
	// 배열 출력
	cout << "1차원 배열 \n";
	for (auto i : arr) {
		cout << i << " ";
	}
	cout << "\n\n";
	cout << "2차원 배열 \n";
	for (const auto& row : matrix) {
		for (const auto& col : row) {
			cout << col << " ";
		}
		cout << "\n";
	}



	return 0;
}