#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int grade;
	cin >> grade;

	if (grade < 60)
		cout << "F";
	else if (grade < 70)
		cout << "D";
	else if (grade < 80)
		cout << "C";
	else if (grade < 90)
		cout << "B";
	else
		cout << "A";

	return 0;
}