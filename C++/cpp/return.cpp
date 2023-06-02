#include<iostream>
#include <array>

using namespace std;

int& get(array<int, 100>& my_array, int ix)
{
	return my_array[ix];
}

int main()
{
	array<int, 100> my_array;
	my_array[30] = 10;

	get(my_array, 30) = 1024;
	cout << my_array[30] << endl;

	return 0;
}