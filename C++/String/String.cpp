#include <string>
#include <iostream>
#include <format>
using namespace std;

string fun1() {
	string myString{ "Hello, World" };

	return myString;
}

void main() {
	string mySt = fun1();

	cout << format("{} \n", fun1());
	cout << format("the value is {} \n", mySt);
	cout << format("the value is {} \n", mySt[1]);
}