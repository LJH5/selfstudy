#include <array>
#include <iostream>
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
	
	// 범위 기반 for
	array arr{ 1, 2, 3, 4 };		// C++
	for (int i : arr) {
		cout << i << " ";
	}
	cout << "\n";
	// 초기자 사용
	for (array arr{ 5, 6, 7, 8 }; int i : arr) {
		cout << i << " ";
	}
	cout << "\n";
}