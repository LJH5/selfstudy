#include <iostream>

using namespace std;


void doSomething(int y)
{
	cout << "In func " << y << " " << &y << endl;
}

void addOne(int &y)
{
	y += 1;
	cout << "In func " << y << " " << &y << endl;
}

void foo(int *ptr) 
{
	cout << "In func " << ptr << " " << &ptr << endl;

}

int main()
{

	// 값에 의한 전달
	cout << "값에 의한 전달" << endl;
	doSomething(5);	
	
	int x = 6;
	cout << "In main " << x << " " << &x << endl;
	doSomething(x);
	
	cout << " " << endl;

	// 참조에 의한 전달 
	cout << "참조에 의한 전달" << endl;
	int z = 5;
	cout << "In main " << z << " " << &z << endl;
	addOne(z);
	cout << "In main " << z << " " << &z << endl;

	cout << " " << endl;

	// 주소에 의한 전달 
	cout << "주소에 의한 전달" << endl;
	int value = 5;
	cout << "In main " << value << " " << &value << endl;
	int* ptr = &value;
	cout << "In main " << &ptr << " " << &value << endl;


	foo(ptr);
	foo(&value);

	return 0;
}