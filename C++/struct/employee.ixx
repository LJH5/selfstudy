// module은 C++20에서 사용이 가능하다
// employee.cppm
export module employee;

export struct Employee {
	char firstInitial;
	char lastInitial;
	int employeeNumber;
	int salary;
};