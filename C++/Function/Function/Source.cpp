#include <iostream>

using namespace std;

int foo(int x, int y);

int foo(int x, int y)
{
	cout << x + y << endl;

	return x + y;
}

int main()
{
	int x = 1, y = 2;

	foo(6, 7);
	foo(x, y + 1);

	return 0;
}