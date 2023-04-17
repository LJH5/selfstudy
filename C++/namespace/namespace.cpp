#include <iostream>

using namespace std;

namespace mycode {
	void foo()
	{
		cout << "foo() called in the mycode namespace \n";
	}
}

using namespace mycode; // 이거 선언 이후 foo()는 모두 mycode의 foo() 임

int main()
{
	mycode::foo();
	foo();	// mycode::foo(); 와 동일한 기능
}