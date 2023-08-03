#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int h, m;
	cin >> h >> m;

	if (m - 45 < 0) {
		m = (60 - 45 + m);
		if (h - 1 < 0) {
			h = 23;
		}
		else
		{
			h -= 1;
		}
	}
	else
	{
		m -= 45;
	}
	cout << h << " " << m;

	return 0;
}