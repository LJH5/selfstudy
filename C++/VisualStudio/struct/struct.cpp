#include <iostream>;
#include <format>;
import employee;

using namespace std;

void main() {
	Employee anEmployee;	//employee.ixx���� �����  struct
	anEmployee.firstInitial = 'J';
	anEmployee.lastInitial = 'H';
	anEmployee.employeeNumber = 33;
	anEmployee.salary = 6000;

	cout << format("Employee: {} {} \n", anEmployee.firstInitial, anEmployee.lastInitial);
	cout << format("Salary: {}���� \n", anEmployee.salary);
}
