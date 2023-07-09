#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	vector<int> v1(3, 5);			// {5, 5, 5};
	cout << v1.size() << "\n";	// 3
	v1.push_back(7);				// {5, 5, 5, 7};
	v1.insert(v1.begin()+1	, 3);	// {5, 3, 5, 5, 7}
	v1.front();							// 5

	for (auto i : v1) {
		cout << i << " ";
	}

	return 0;
}