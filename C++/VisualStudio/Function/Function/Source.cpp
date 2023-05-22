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

	// ���� ���� ����
	cout << "���� ���� ����" << endl;
	doSomething(5);	
	
	int x = 6;
	cout << "In main " << x << " " << &x << endl;
	doSomething(x);
	
	cout << " " << endl;

	// ������ ���� ���� 
	cout << "������ ���� ����" << endl;
	int z = 5;
	cout << "In main " << z << " " << &z << endl;
	addOne(z);
	cout << "In main " << z << " " << &z << endl;

	cout << " " << endl;

	// �ּҿ� ���� ���� 
	cout << "�ּҿ� ���� ����" << endl;
	int value = 5;
	cout << "In main " << value << " " << &value << endl;
	int* ptr = &value;
	cout << "In main " << &ptr << " " << &value << endl;


	foo(ptr);
	foo(&value);

	return 0;
}