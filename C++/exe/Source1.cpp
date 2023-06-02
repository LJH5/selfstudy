#include<iostream>
#include <array>

using namespace std;

struct S
{
	int a, b, c, d;
};

S getStruct()
{
	S my_s{ 1, 2, 3, 4 };
}

int main() 
{
	S my_s = getStruct();
	my_s.b;

}