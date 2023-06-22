#include <iostream>
#include <vector>

using namespace std;

int main(void) {
	vector<int> v(100);
	v[101] = 100;
	
	cout << v[101];

	return 0;
}