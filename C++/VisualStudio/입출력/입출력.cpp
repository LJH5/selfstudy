// C++20 ���� ���� import <iostream>; 
#include <iostream>
#include <format>

using namespace std;

void main()
{
	// �Է�
	int value;
	cin >> value;
	int num;
	scanf("%d", &num); // C���� ����ϴ� ��� C++������ ����,  cin���� �ӵ��� �������� �������� ����

	// ���
	cout << "Hello, World!" << endl;	// ���� std�� �����ؼ� 'std::'�� ������ �ʾƵ� ��  
	cout << "Hello, World!" << "\n";		// endl�� \n�� ����� ������
	std::cout << "There are " << value << " ways, I love you." << std::endl;	// ���� ���	
	std::cout << std::format("There are {} ways, I love you.", value) << std::endl; //C++20 ����
	printf("%d", &num); // C���� ����ϴ� ��� C++������ ����,  cout���� �ӵ��� �������� �������� ����
}