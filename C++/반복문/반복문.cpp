#include <iostream>
#include <array>
using namespace std;

int main() {
	//while
	int a{ 0 };
	while (a < 5) {
		cout << "This is silly \n";
		++a;
	}
	cout << "\n";

	// do/while
	int b{ 100 };
	do {
		cout << "This is silly \n";
		++b;
	} while (b < 5);
	cout << "\n";

	// for
	for (int c { 0 }; c < 5; ++c ) {
		cout << "This is silly \n";
	}
	
	// 범위 기반 for 문
	array arr{ 1, 2, 3, 4 };
	for (int i : arr) {
		cout << i << "\n";
	}

}