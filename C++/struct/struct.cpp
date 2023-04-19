#include <iostream>;
#include <format>;
import employee;

using namespace std;

void main() {
	Employee anEmployee;	//employee.ixx에서 선언된  struct
	anEmployee.firstInitial = 'J';
	anEmployee.lastInitial = 'H';
	anEmployee.employeeNumber = 33;
	anEmployee.salary = 6000;

	cout << format("Employee: {} {} \n", anEmployee.firstInitial, anEmployee.lastInitial);
	cout << format("Salary: {}만원 \n", anEmployee.salary);
}
