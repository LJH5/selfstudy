#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m, target_r, target_c;
	cin >> n >> m;
	
	char people_arr[601][601] = {};

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> people_arr[i][j];
			if (people_arr[i][j] == 'I') {
				target_r = i, target_c = j;
			}
		}
	}


	return 0;
}